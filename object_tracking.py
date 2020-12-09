import cv2
import numpy as np

# name of five sequences and the number of frames for each sequences
file_list = {'bookI': 531,
             'bookII': 577,
             'bookIII': 653,
             'bus': 726,
             'cereal': 497}

# Lucas kanade params
lk_params = dict(winSize=(32, 32),
                 maxLevel=4,
                 criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

for f in file_list:
    print(f)
    number_frame = file_list[f]
    file_path = f

    # read ground truth file and save ground truth into list
    ground_truth_file = 'ground_truth/' + f + '.txt'
    file = open(ground_truth_file, 'r')
    lines = file.readlines()
    ground_truth = []

    # strips the newline into list
    for line in lines:
        ulx, uly, urx, ury, lrx, lry, llx, lly = line.strip().split()
        # saving the bounding box start and end coordinates
        ground_truth.append((ulx, uly, urx, ury, lrx, lry, llx, lly))

    # Use the ground truth file for the image in the first time point to initialize the tracker
    ulx, uly = float(ground_truth[0][0]), float(ground_truth[0][1])
    urx, ury = float(ground_truth[0][2]), float(ground_truth[0][3])
    lrx, lry = float(ground_truth[0][4]), float(ground_truth[0][5])
    llx, lly = float(ground_truth[0][6]), float(ground_truth[0][7])

    # initialize first points and first frame
    old_points = np.array([[ulx, uly], [urx, ury], [lrx, lry], [llx, lly]], dtype=np.float32)
    img = cv2.imread(file_path + '/img001.jpg')
    old_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    tracker_output = []
    difference = 0

    for i in range(number_frame):
        # load img file
        frame = '%03d' % int(i + 1)
        file_name = '/img' + frame + '.jpg'
        img = cv2.imread(file_path + file_name)
        gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # draw tracker output in red rectangle
        new_points, status, error = cv2.calcOpticalFlowPyrLK(old_gray, gray_frame, old_points, None, **lk_params)
        old_gray = gray_frame.copy()
        old_points = new_points
        ulx, uly, urx, ury, lrx, lry, llx, lly = new_points.ravel()
        pts = np.array([[ulx, uly], [urx, ury], [lrx, lry], [llx, lly]], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, (0, 0, 255), 2)
        tracker_output.append((ulx, uly, urx, ury, lrx, lry, llx, lly))

        # draw ground truth in green rectangle
        gt_ulx, gt_uly = int(float(ground_truth[i][0])), int(float(ground_truth[i][1]))
        gt_urx, gt_ury = float(ground_truth[i][2]), float(ground_truth[i][3])
        gt_lrx, gt_lry = float(ground_truth[i][4]), float(ground_truth[i][5])
        gt_llx, gt_lly = float(ground_truth[i][6]), float(ground_truth[i][7])
        pts = np.array([[gt_ulx, gt_uly], [gt_urx, gt_ury], [gt_lrx, gt_lry], [gt_llx, gt_lly]], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, (0, 255, 0), 2)

        # calculate euclidean distance between ground truth and tracker output
        gt_ul = np. array((ground_truth[i][0], ground_truth[i][1]), dtype=np.float32)
        ul = np. array((ulx, uly), dtype=np.float32)
        gt_ur = np.array((ground_truth[i][2], ground_truth[i][3]), dtype=np.float32)
        ur = np.array((urx, ury), dtype=np.float32)
        gt_lr = np.array((ground_truth[i][4], ground_truth[i][5]), dtype=np.float32)
        lr = np.array((lrx, lry), dtype=np.float32)
        gt_ll = np.array((ground_truth[i][6], ground_truth[i][7]), dtype=np.float32)
        ll = np.array((llx, lly), dtype=np.float32)
        dist = np.linalg.norm(gt_ul - ul) + np.linalg.norm(gt_ur - ur) + np.linalg.norm(gt_lr - lr) + np.linalg.norm(gt_ll - ll)

        difference += dist

        # show results
        font = cv2.FONT_HERSHEY_DUPLEX
        font_size = 0.65
        pos_x = 20
        img = cv2.putText(img, 'Current video: ' + file_path, (pos_x, 544), font, font_size, (0, 255, 0), 1, cv2.LINE_AA)
        img = cv2.putText(img, 'Ground truth in green rectangle', (pos_x, 564), font, font_size, (0, 255, 0), 1, cv2.LINE_AA)
        img = cv2.putText(img, 'Tracker output in red rectangle', (pos_x, 584), font, font_size, (0, 0, 255), 1, cv2.LINE_AA)
        cv2.imshow('frame', img)
        cv2.waitKey(1)
    print("Sum of Euclidean distance: " + str(difference))

    # save both .npy and .txt file with the bounding box coordinates of the tracked objects in the format:
    # ulx, uly, urx, ury, lrx, lry, llx, lly:
    np.save('object_tracking_results/' + file_path + '.npy', np.array(tracker_output))
    np.savetxt('object_tracking_results/' + file_path + '.txt', np.array(tracker_output), fmt='%d')
