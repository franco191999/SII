/**
*
* Jquery Mapael - Dynamic maps jQuery plugin (based on raphael.js)
* Requires jQuery and raphael.js
*
* Map of World by country
* 
* @source http://backspace.com/mapapp/javascript_world/
*/

(function($) {
	$.extend(true, $.fn.mapael, 
		{
			maps :  {
				world_countries : {
					width : 1000,
					height : 400,
					getCoords : function (lat, lon) {
						var xfactor = 2.752;
						var xoffset = 473.75;
						var x = (lon * xfactor) + xoffset;
						
						var yfactor = -2.753;
						var yoffset = 231;
						var y = (lat * yfactor) + yoffset;
						
						return {x : x, y : y};
					},
					'elems': {
						"CU" : "M247.326,167.081l2.326,0.290l2.326,0.000l2.325,0.871l1.163,1.161l2.616,-0.290l0.873,0.581l2.325,1.743l1.744,1.161l0.871,0.000l1.744,0.581l-0.290,0.871l2.035,0.000l2.325,1.161l-0.581,0.581l-1.744,0.291l-1.745,0.290l-2.035,-0.290l-3.778,0.290l1.743,-1.452l-1.161,-0.871l-1.744,0.000l-0.872,-0.871l-0.582,-1.742l-1.744,0.289l-2.616,-0.870l-0.582,-0.581l-3.779,-0.291l-0.872,-0.581l0.872,-0.580l-2.616,-0.290l-2.034,1.451l-1.163,0.000l-0.292,0.580l-1.452,0.292l-1.163,0.000l1.454,-0.872l0.581,-1.161l1.453,-0.581l1.163,-0.581l2.325,-0.290l-0.581,0.290z",
						
					}
				}
			}
		}
	);
})(jQuery);
