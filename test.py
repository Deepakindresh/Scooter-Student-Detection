from ultralytics import YOLO


model = YOLO("best.pt")

results = model.predict(source="http://10.13.143.162:8080/video", show=True)

print(results)
# print(type(results))
# for r in results:
#      boxes = r.boxes  # Boxes object for bbox outputs
#      masks = r.masks  # Masks object for segment masks outputs
#      probs = r.probs  # Class probabilities for classification outputs
#      print("This is boxes", boxes)
#      print("This is masks", masks)
#      print("This is probs", probs)