
(function () {
  'use strict';
  angular
      .module('MyApp',['ngMaterial', 'ngMessages', 'material.svgAssetsCache'])
      .controller('DemoCtrl', DemoCtrl)
      .filter('num', function() {
    return function(input) {
      return parseInt(input, 10);
    };
})
      .config(function($mdThemingProvider) {
  $mdThemingProvider.theme('dark-grey').backgroundPalette('grey').dark();
  $mdThemingProvider.theme('dark-orange').backgroundPalette('orange').dark();
  $mdThemingProvider.theme('dark-purple').backgroundPalette('deep-purple').dark();
  $mdThemingProvider.theme('dark-green').backgroundPalette('green').dark();
  $mdThemingProvider.theme('dark-yellow').backgroundPalette('yellow');
});

  function DemoCtrl ($log, $http, $scope) {
    var self = this;
    self.model = {
            days: [
            "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"

            ],
            times: {
              "1": {
                  "start_time": "08:00",
                  "end_time": "08:50"
              },
              "2": {
                  "start_time": "09:00",
                  "end_time": "09:50"
              },
              "3": {
                  "start_time": "10:00",
                  "end_time": "10:50"
              },
              "4": {
                  "start_time": "11:00",
                  "end_time": "11:50"
              },
              "5": {
                  "start_time": "12:10",
                  "end_time": "13:00"
              },
              "6": {
                  "start_time": "13:10",
                  "end_time": "14:00"
              },
              "7": {
                  "start_time": "14:10",
                  "end_time": "15:00"
              },
              "8": {
                  "start_time": "15:10",
                  "end_time": "16:00"
              },
              "9": {
                  "start_time": "16:10",
                  "end_time": "17:00"
              },
              "10": {
                  "start_time": "17:20",
                  "end_time": "18:10"
              },
              "11": {
                  "start_time": "18:30",
                  "end_time": "19:20"
              },
              "12": {
                  "start_time": "19:30",
                  "end_time": "20:20"
              },
              "13": {
                  "start_time": "20:30",
                  "end_time": "21:20"
              },
              "14": {
                  "start_time": "21:30",
                  "end_time": "22:20"
              }
            }
        };
    self.querySearch = querySearch;
    self.choice = {a: null};
    // ******************************
    // Internal methods
    // ******************************
    $scope.rep = function(value) {
      var arr=[];
      for (item in value) {
        arr.push(item.number);
      }
      $log.info("hello");
      return arr;
    }
    function querySearch (query) {
    return $http.get('/search/?query=' + query).then(function(response) {
            return response.data;
           });
    }

    $scope.submit = function() {
      var query=self.choice.a.id;

      $http.get('/' + self.choice.a.type + '/' + query).then(function(response) {
          
          self.model.items=response.data;
           });
    }
    $scope.day = function() {
      var d = new Date();
      var n = d.getDay();
      return n;
    }
  
  }
})();


/**
Copyright 2016 Google Inc. All Rights Reserved. 
Use of this source code is governed by an MIT-style license that can be foundin the LICENSE file at http://material.angularjs.org/HEAD/license.
**/