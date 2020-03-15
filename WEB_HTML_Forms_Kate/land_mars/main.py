from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/carousel')
def Mars():
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <title>Bootstrap Example</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
<link rel="stylesheet" href="{url_for('static', filename='css/style1.css')}">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
</head>
<body>

<div class="container">
  <br>
  <div id="myCarousel" class="carousel slide" data-ride="carousel">
    <!-- Indicators -->
    <ol class="carousel-indicators">
      <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
      <li data-target="#myCarousel" data-slide-to="1"></li>
      <li data-target="#myCarousel" data-slide-to="2"></li>
    </ol>

    <div class="carousel-inner" role="listbox">
    <div class="item active">
      <img src="{url_for('static', filename='img/Painting_Art_Mars_Ships_USSR_570703_1280x720.jpg')}" alt="Chania">
      <div class="carousel-caption">
      </div>
    </div>


    <div class="item">
      <img src="{url_for('static', filename='img/Ds8z8PsUwAAdmzJ.jpg')}" alt="Flower">
      <div class="carousel-caption">
      </div>
    </div>

    <div class="item">
      <img src="{url_for('static', filename='img/434219-Kycb.jpg')}" alt="Flower">
      <div class="carousel-caption">
      </div>
    </div>
  </div>

    <a class="left carousel-control" href="#myCarousel" role="button" data-slide="prev">
      <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
      <span class="sr-only">Previous</span>
    </a>
    <a class="right carousel-control" href="#myCarousel" role="button" data-slide="next">
      <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
      <span class="sr-only">Next</span>
    </a>
  </div>
</div>

</body>
</html>

'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
