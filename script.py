import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'schedule.settings')
import django

django.setup()

import requests
import json
import pprint
from core.models import *
from datetime import datetime
from collections import OrderedDict

if __name__ == "__main__":
    # url = "http://schedule.iitu.kz/rest/user/get_timetable_block.php"
    url = "http://schedule.iitu.kz/rest/user/get_timetable_room.php"
    # for i in range(13765, 14246):
    for i in range(0, 500):

        # querystring = {"block_id": str(i)}
        querystring = {"bundle_id": str(i)}

        response = requests.request("GET", url, params=querystring)
        # print(response.status_code)
        e = response.text
        a = json.loads(e)
        # some = json.loads(e, object_pairs_hook=OrderedDict)
        bl = a['blocks']
        bd = a['bundles']
        s = a['subjects']
        b = a['timetable']
        t = a['teachers']
        if not b:
            continue
        # print(i)
        # pp = pprint.PrettyPrinter(indent=4)
        # pp.pprint(a)
        bls = sorted(bl)
        # print(bl)
        value = bl[bls[0]]
        u = Block.objects.get_or_create(name=value['name'])[0]
        # print(u.name)
        # for item in bls:
        #     # print(value['name'])
        #     value = bl[item]
        #     k = Block.objects.get_or_create(name=value['name'])[0]
        #     u.my.add(k)
        #     # print(value['name'])

        for key, value in s.items():
            # print(value['subject_en'])
            Subject.objects.get_or_create(name=value['subject_en'])

        for key, value in t.items():
            # print(value['teacher_en'])
            Tutor.objects.get_or_create(name=value['teacher_en'])

        for key, value in bd.items():
            bundle = Bundle.objects.get_or_create(ID=int(key))
            if bundle[1]:
                for key, value in value.items():
                    if key == 'name':
                        for item in value:
                            room = Room.objects.get_or_create(number=item['name_en'])
                            bundle[0].room.add(room[0])
                    if key == '0':
                        room = Room.objects.get_or_create(number=value['name_en'])
                        bundle[0].room.add(room[0])

        for key, value in b.items():
            # print(key)
            for key1, value in value.items():
                c = value[0]  # slovar table

                id = c['subject_id']
                # print(a['subjects'][id]['subject_en'])
                subject = Subject.objects.get(name=a['subjects'][id]['subject_en'])
                # print(subject)

                time = c["time_id"]
                start = a['times'][time]['start_time']
                start = datetime.strptime(start, '%H:%M:%S').time()
                end = a['times'][time]['end_time']
                end = datetime.strptime(end, '%H:%M:%S').time()
                day = int(key)
                # print("day ", day)

                id = c["teacher_id"]
                tutor = a['teachers'][id]["teacher_en"]

                ID = c['bundle_id']
                bundle = Bundle.objects.get(ID=int(ID))

                tutor = Tutor.objects.get(name=tutor)

                block = c['block_id']
                block = Block.objects.get(name=bl[block]['name'])
                # print(time)
                time = Time.objects.get(pk=int(time))
                # print(block.name)
                some, created = Table.objects.update_or_create(
                    subject=subject,
                    start=start,
                    end=end,
                    block=block,
                    tutor=tutor,
                    bundle=bundle,
                    day=day,
                    defaults={'time': time}
                )
                # print(created)