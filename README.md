<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Site Title{% endblock %}</title>

    <style>
        /* Reset some default browser styles */
        body, h1, h2, h3, p, ul, li {
            margin: 0;
            padding: 0;
        }

        /* Set HTML and body to full height */
        html, body {
            height: 100%;
        }

        /* Use flexbox on body */
        body {
            display: flex;
            flex-direction: column;
            background-image: url("/static/images/st.jpg"); /* Correct path format */
            background-size: cover; /* Make the background cover the entire page */
            background-repeat: no-repeat; /* Prevent the background from repeating */
            background-attachment: fixed; /* Fix the background image in place */
            background-color: #114d0f; /* Light gray */
        }

        /* Main content should expand to fill available space */
        .container {
            flex: 1;
            max-width: 800px;
            margin: 20px auto;
            padding: 20px;
            background-color: #ee952f; /* White */
            border-radius: 5px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1); /* Light shadow */
        }

        /* Style navigation */
        nav {
            background-color: #e9e634; /* Dark gray */
            padding: 50px 0;
        }

        nav ul {
            list-style-type: none;
            text-align: center;
        }

        nav ul li {
            display: inline;
            margin-right: 20px;
        }

        nav ul li a {
            text-decoration: none;
            color: #db0c28; /* White */
            font-weight: bold;
            font-size: 30px;
            margin: 10px;
            /* border: 1px solid #b5eb37; */
            padding: 5px;
        }

        nav ul li a:hover {
            color: #ee8c0d; /* Light gray */
        }

        /* Style footer */
        footer {
            text-align: center;
            padding: 10px;
            background-color: #343a40; /* Dark gray */
            color: #ffffff; /* White */
        }

        /* Style flash messages */
        .flash-messages {
            list-style-type: none;
            margin-top: 20px;
            padding: 10px;
            background-color: #040922; /* Blue */
            color: #e91313; /* White */
            border-radius: 5px;
            height: 5%;
            font-size: 30px;
        }

        .flash-messages li {
            margin-bottom: 5px;
        }
    </style>

</head>
<body>
    <nav>
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/Employees directory">Employees directory</a></li>
            <li><a href="/profile">Profile</a></li>
            <li><a href="/Materials">Materials</a></li>
            <li><a href="/logout">Logout</a></li>
            <li><a href="/login">Login</a></li>
            <li><a href="/register">Register</a></li>
            <li><a href="/Work plan">Work plan</a></li>
        </ul>
    </nav>
    
    <div class="container">
        living in style
        <!-- Default content if not overridden by child templates -->
        <h1>Welcome Sunpark Site Management System</h1>
        <img src="/static/images/image1.jpg" alt="Description of the image" style="max-width: 100%; height: auto;">
    
    </div>

    <footer>
        <p>&copy; 2024 Your Company. All rights reserved.</p>
    </footer>


            <ul class="flash-messages">
        
                    <li>safty starts with you</li>
            </ul>

    <script src="{{ url_for('static', filename='script.js') }}"></script>
</body>
</html>
