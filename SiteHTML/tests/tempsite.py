import tempfile
import os.path
import os

__author__ = 'ethan'

index_content = """<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title>Home</title>
    <!-- Begin Global head -->
    <meta name="viewport" content="initial-scale=1.0, user-scalable=yes, width=device-width">
    <link rel="stylesheet" type="text/css" href="css/style.css">
    <!-- End Global head -->
</head>
<body>
<!-- Begin Global header element -->
<header>
    <nav>
        <ul>
            <li><a href="index.html">Home</a></li>
            <li><a href="contact.html">Contact Us</a></li>
        </ul>
        <span id="domain_banner">Wirehopper.net<span id="subdomain">/~ethan</span></span>
    </nav>
</header>
<!-- End Global header element -->
<section>
    <h1>Home</h1>
</section>
<!-- Begin Global footer element -->
<footer>
</footer>
<script type="text/javascript" src="js/page.js"></script>
<!-- End Global footer element -->
</body>
</html>
"""

blank_content = """<!DOCTYPE html>
<html>
<head lang="en">
    <!-- Begin Global head element -->
    <meta charset="UTF-8">
    <!-- End Global head element -->
    <title></title>
</head>
<body>
<!-- Begin Global header element -->
<header>
    <nav>
    <!-- Begin Global footer element -->
    </nav>
</header>
<!-- End Global header element -->

<!-- Begin Global footer element -->
<footer>
</footer>
<!-- End Global footer element -->
</body>
</html>
"""

blank_content2 = """<!DOCTYPE html>
<html>
<head lang="en">
    <!-- Begin Global head element -->
    <meta charset="UTF-8">
    <!-- End Global head element -->
    <title></title>
</head>
<body>
<!-- Begin Global header element -->
<header>
    <nav>
    </nav>
</header>
<!-- End Global header element -->

<!-- Begin Global footer element -->
<footer>
</footer>
<!-- End Global footer element -->
</body>
</html>
"""


class TestSite:
    def __init__(self):
        self.t_d = os.path.realpath(tempfile.mkdtemp())
        self.samples_fps = []
        self.samples_fds = []
        self.make_sample_files()
        self.samples_fds[0].write(index_content)
        self.samples_fds[1].write(blank_content2)
        for fd in self.samples_fds[2:]:
            fd.write(blank_content)
        for fd in self.samples_fds:
            fd.seek(0)

    def make_sample_files(self):
        for x in ['index.html', 'page1.html', 'page2.html', 'page3.html']:
            t_fp = os.path.join(self.t_d, x)
            t_fd = open(t_fp, 'w+r')
            self.samples_fps.append(t_fp)
            self.samples_fds.append(t_fd)

    def cleanup(self, delete=False):
        for fp, fd in zip(self.samples_fps, self.samples_fds):
            if not fd.closed:
                fd.close()
            if delete:
                os.remove(fp)
        if delete:
            os.rmdir(self.t_d)