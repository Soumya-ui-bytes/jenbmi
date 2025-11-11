import sys
if len(sys.argv) == 3:
  script_name = sys.argv[0]
  weight = float(sys.argv[1])
  height = float(sys.argv[2])
  bmi = weight / (height * height)
  print("user provided input values:")
  print("script name:", script_name)
  print("weight:", weight)
  print("height:", height)
  bmi = weight / (height * height)
  print("bmi:",bmi)
else:
  script_name = sys.argv[0]
  weight = "49"
  height = "180"
  print("no input given:")
  print("script name:", script_name)
  print("weight:", weight)
  print("height:", height)
  bmi = weight / (height * height)
  print("bmi:",bmi)
