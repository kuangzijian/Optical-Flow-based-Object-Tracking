
<!-- PROJECT LOGO
<br />
<p align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Best-README-Template</h3>

  <p align="center">
    An awesome README template to jumpstart your projects!
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a>
  </p>
</p>
-->


<!-- TABLE OF CONTENTS 
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)
-->


<!-- ABOUT THE PROJECT -->
## Optical-Flow-based-Object-Tracking

This project focuses on topics:
* Use optical flow to track the object

### Built With
* [OpenCV](https://opencv.org/)
* [Numpy](https://numpy.org/)

### Prerequisites
```sh
1. Clone the repo
2. pip install -r requirements.txt
3. Make sure your folder structure is like the screenshot below:
![structure](https://github.com/kuangzijian/UAlberta-Multimedia-Master-Program-MM811-2020-Assignment-3/blob/main/images/after.png)

```

### Optical Flow based Object Tracking
```
python object_tracking.py 

The output will show both ground truth bounding box and the bounding box created by the object tracker:
![ouput1](https://github.com/kuangzijian/UAlberta-Multimedia-Master-Program-MM811-2020-Assignment-3/blob/main/images/after.png)

The program also save both .npy and .txt files with the bounding box coordinates of the tracked objects in the format: 
ulx, uly, urx, ury, lrx, lry, llx, lly:
![ouput2](https://github.com/kuangzijian/UAlberta-Multimedia-Master-Program-MM811-2020-Assignment-3/blob/main/images/after.png)
```

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

## References
OpenCV object tracking: 
