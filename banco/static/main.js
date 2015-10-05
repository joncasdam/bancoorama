console.log('aqui!');

angular.module('DashbaordApp.services', [])
  .factory('saqueAPIservice', function($http) {

    var ergastAPI = {};

    ergastAPI.getDrivers = function() {
      return $http({
        method: 'JSONP',
        url: 'http://ergast.com/api/f1/2015/driverStandings.json?callback=JSON_CALLBACK'
      });
    }

    ergastAPI.getDriverDetails = function(id) {
      return $http({
        method: 'JSONP',
        url: 'http://ergast.com/api/f1/2015/drivers/'+ id +'/driverStandings.json?callback=JSON_CALLBACK'
      });
    }

    ergastAPI.getDriverRaces = function(id) {
      return $http({
        method: 'JSONP',
        url: 'http://ergast.com/api/f1/2015/drivers/'+ id +'/results.json?callback=JSON_CALLBACK'
      });
    }

    return ergastAPI;
  });

angular.module('F1FeederApp.controllers', []).
  controller('dashobardController', function($scope, ergastAPIservice) {
    $scope.nameFilter = null;
    $scope.driversList = [];
    $scope.searchFilter = function (driver) {
        var re = new RegExp($scope.nameFilter, 'i');
        return !$scope.nameFilter || re.test(driver.Driver.givenName) || re.test(driver.Driver.familyName);
    };

    ergastAPIservice.getDrivers().success(function (response) {
        //Digging into the response to get the relevant data
        $scope.driversList = response.MRData.StandingsTable.StandingsLists[0].DriverStandings;
    });
  });


app.controller('dashboardController', function($scope, $http){
	$scope.formData = {};

	$scope.onSubmit = function(valid){
		console.log($scope.formData);

		$http.post('https://minmax-server.herokuapp.com/register/', $scope.formData).
			success(function (data){
				console.log('foi')
			}).error(function (data){
				console.log('deu ruim')
		});
	}

});