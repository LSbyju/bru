import cv2

def drawBox(img, bbox):
    x, y, w, h = bbox
    cv2.rectangle(img, (x, y), (x+w, y+h), (255,0,0), 2)
    cv2.putText(img, "Tracking", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 2)

def goal_track(img, bbox):
    # code for goal tracking
    pass

# initialize tracker
tracker = cv2.TrackerMOSSE_create()

# read video
cap = cv2.VideoCapture(0)

# read first frame
success, img = cap.read()

# select the bounding box of the object to be tracked
bbox = cv2.selectROI(img, False)

# initialize tracker
tracker.init(img, bbox)

while True:
    # read video
    success, img = cap.read()
    
    # update tracker
    success, bbox = tracker.update(img)
    
    # check if success
    if success:
        drawBox(img, bbox)
        goal_track(img, bbox)
    else:
        cv2.putText(img, "LOST", (100,200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
    
    # show frame
    cv2.imshow("Tracking", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release video and close all windows
cap.release()
cv2.destroyAllWindows()
