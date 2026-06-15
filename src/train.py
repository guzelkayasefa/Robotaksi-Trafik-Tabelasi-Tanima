from ultralytics import YOLO

def main():
    
    model = YOLO("yolo11s.pt")

    
    results = model.train(
        data="dataset/data.yaml", 
        epochs=95,
        imgsz=960,
        batch=16,
        device=0,
        mosaic=1.0,      
        scale=0.5,      
        hsv_s=0.7,      
        hsv_v=0.4,       
        project="runs",         
        name="yolo11s_train"    
    )

if __name__ == '__main__':
    main()