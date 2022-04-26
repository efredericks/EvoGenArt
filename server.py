from flask import Flask, render_template
import random

### CLASS THIS OUT!!!
import tracery
rules = {
  "shapes": [
    # "arc(#arcParams#)",
    # "ellipse(#ellipseParams#)",
    "circle(#circleParams#)",
    # "line(#lineParams#)",
    # "point(#pointParams#)",
    # "quad(#quadParams#)",
    # "rect(#rectParams#)",
    # "square(#squareParams#)",
    # "triangle(#triangleParams#)",
  ],
  # https://p5js.org/reference/#/p5/arc
  "arcParams": [
    "#int#, #int#, #int#, #int#, #float#, #float#",
    "#int#, #int#, #int#, #int#, #float#, #float#, #arcMode#, #arcDetail#",
  ],
  "arcMode": ["CHORD", "PIE", "OPEN"],
  "arcDetail": "0", #0-50

  # https://p5js.org/reference/#/p5/ellipse
  "ellipseParams": [
    "#int#, #int#, #int#", # ellipse(x, y, w])
    "#int#, #int#, #float#, #float#", # ellipse(x, y, w, h)
    # skipping [detail] -> WebGL only
  ],

  # https://p5js.org/reference/#/p5/circle
  "circleParams": "{x}, {y}, {d}",
  # "circleParams": "#int#, #int#, #float#",

  # https://p5js.org/reference/#/p5/line
  "lineParams": "#int#, #int#, #int#, #int#",

  # https://p5js.org/reference/#/p5/point
  "pointParams": "#int#, #int#",

  # https://p5js.org/reference/#/p5/quad
  "quadParams": [
    # quad(x1, y1, x2, y2, x3, y3, x4, y4, [detailX], [detailY])
    "#int#, #int#, #int#, #int#, #int#, #int#, #int#, #int#",
    "#int#, #int#, #int#, #int#, #int#, #int#, #int#, #int#, #int#, #int#",
  ],

  # https://p5js.org/reference/#/p5/rect
  "rectParams": [
    "#int#", "#int#", "#float#",
    "#int#", "#int#", "#float#, #float#",
    "#int#", "#int#", "#float#, #float#, #float#,",
    "#int#", "#int#", "#float#, #float#, #float#, #float#",
    "#int#", "#int#", "#float#, #float#, #float#, #float#, #float#",
    "#int#", "#int#", "#float#, #float#, #float#, #float#, #float#, #float#",
  ],

  # https://p5js.org/reference/#/p5/square
  "squareParams": [
    "#int#, #int#, #int#",
    "#int#, #int#, #int#, #float#",
    "#int#, #int#, #int#, #float#, #float#",
    "#int#, #int#, #int#, #float#, #float#, #float#",
    "#int#, #int#, #int#, #float#, #float#, #float#, #float#",
  ],

  # https://p5js.org/reference/#/p5/triangle
  "triangleParams": "#int#, #int#, #int#, #int#, #int#, #int#",

  "int": "1",
  "float": "1.1",
}
#####

app = Flask(__name__)

@app.route("/")
def index():
  grammar = tracery.Grammar(rules)

  width = 200
  height = 200

  details = []
  numSketches = random.randint(1,20)

  for i in range(numSketches):
    d = random.randint(10,100)
    x = random.randint(d,width-d)
    y = random.randint(d,height-d)

    deets = {
      'x':x,
      'y':y,
      'd':d,
    }
    shape = grammar.flatten("#shapes#").format(**deets)

    dt = {
      'bg': [random.randint(0,255),random.randint(0,255), random.randint(0,255)],
      'shape': shape
    }
    details.append(dt)

  templateData = {
    'width': width,
    'height': height,
    'numSketches': numSketches,
    'details': details
  }
  print(templateData)
  return render_template('index.html', **templateData)


if __name__ == "__main__":
  app.run(host='0.0.0.0', port='8080', debug=True)