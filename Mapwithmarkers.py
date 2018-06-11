from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    head = """<!DOCTYPE html>
    <html> 
    <head> 
      <meta http-equiv="content-type" content="text/html; charset=UTF-8" /> 
      <title>Dopespots Around Opechee</title> 
      <script src="http://maps.google.com/maps/api/js?sensor=false" 
              type="text/javascript"></script>
        <img src="https://rocherealty.com/wp-content/uploads/2016/11/Round_Bay_Rd_21.jpg" width="225" height="122" align="right">
        <img src="https://rocherealty.com/wp-content/uploads/2016/11/Round_Bay_Rd_21.jpg" width="225" height="122" align="left">

    </head>
    <body>
    <style>
    body{
        background-color: #228B22;
    }
    </style>
    <p><font size="8"><center>Dopespots</font></p>
    <center>Popular dope spots based around Lake Opechee
    <center>includes parks, fields, rope swings, walking paths, and fishing areas
    <p><center><p>
    
      <div id="map" style="width: 1300px; height: 515px;"></div>
    """

    d = []
    middle2 = ''
    middle1 = """<script type="text/javascript">
        var locations = [\n"""
    for line in open('Locations.txt'):
        line = line.strip()
        d = line.split('\t')
        middle2 += "\t[{}, {}, {}, {}, {}],\n".format(d[0], d[1], d[2], d[3], d[4])
    middle3 = """\n        ];"""
    middle = middle1 + middle2 + middle3
    tail = """
            var map = new google.maps.Map(document.getElementById('map'), {
              zoom: 13,
              center: new google.maps.LatLng(43.546236, -71.473124),
              mapTypeId: google.maps.MapTypeId.ROADMAP
            });

            var infowindow = new google.maps.InfoWindow();

            var marker, i;

            for (i = 0; i < locations.length; i++) {  
              marker = new google.maps.Marker({
                position: new google.maps.LatLng(locations[i][1], locations[i][2]),
                map: map
              });

              google.maps.event.addListener(marker, 'click', (function(marker, i) {
                return function() {
                  infowindow.setContent(locations[i][0] + "<br>" + locations[i][4]);
                  infowindow.open(map, marker);
                }
              })(marker, i));
            }
          </script>
        </body>
        </html>"""
    returnvalue = head + middle + tail
    return returnvalue
#print(index())

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)
