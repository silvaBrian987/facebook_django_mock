"use strict";

(function(){
	var app = angular.module("app", []);

	app.run(function($rootScope, $http, $log){
		$log.info("App run!!!")

		let $document = angular.element(document);

		$rootScope.loginFB = function(){
			$http.get('loginFB/').then(function(response){
				$log.info(response);
				if(response.data.loginURL){
					//window.location.href = response.data.loginURL;
					$rootScope.showIframe = true;
					$document.find("body").find("a").attr("href", response.data.loginURL);
					$document.find("body").find("a")[0].innerHTML="Acceso a facebook"
				}
			});
		}
	});
})(angular);