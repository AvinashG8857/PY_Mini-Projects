import cv2
from ultralytics import YOLO
import sys

def run_detection():
    
    try:
        print("Loading YOLO model...")
        model = YOLO('yolov8n.pt') 
        print("Model loaded successfully.")
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        return

    
    print("Attempting to open camera...")
    cap = cv2.VideoCapture(0) # 0 is default. Try 1 if 0 fails.

    if not cap.isOpened():
        print("❌ Error: Could not open webcam. Check permissions or if another app is using it.")
        return
    else:
        print("✅ Camera opened successfully.")

    
    while True:
        success, frame = cap.read()
        
        if not success:
            print("❌ Failed to grab frame.")
            break

        # Run detection
        
        results = model(frame, verbose=True) 

        
        annotated_frame = results[0].plot()
 
        
        cv2.imshow("YOLOv8 Detection", annotated_frame)

        # Wait for 1ms and check if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            print("Closing application...")
            break

    # CLEANUP
    cap.release()
    cv2.destroyAllWindows()
    # Explicitly call these to force windows to close on some systems
    for i in range(1, 5):
        cv2.waitKey(1)

if __name__ == "__main__":
    run_detection()