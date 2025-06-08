# [olivineoverlord.github.io/](https://olivineoverlord.github.io/)
## Personal Academic Website

This repository contains the source code for my personalised academic website. It presents my research, blog, academic profile, and contact details in a minimalist, responsive format that is easy to maintain and deploy.

## Design Philosophy

This site is intentionally minimal. It avoids the use of frameworks or JavaScript-heavy elements in order to remain lightweight, fast-loading, and easy to maintain. The structure emphasises clarity, and long-term portability.

## Features
- Semantic and accessible HTML
- Custom CSS with responsive layout
- Light/dark mode toggle (JavaScript)
- Static blog system (HTML-based)
- No frameworks or build tools
- Deployable via GitHub Pages

## Live Site

You can visit the live site at: [olivineoverlord.github.io/](https://olivineoverlord.github.io/)

## File Structure

```
/
├── index.html              # Homepage
├── about.html              # About
├── research.html           # Research summary
├── blog/                   # Blog posts
│   ├── post1.html
│   └── ...
│   └── post.js             # Blog logic
├── contact.html            # Contact details
├── css/
│   └── styles.css          # Main stylesheet
├── assets/
│   ├── images/             # Static images
│   └── documents/          # Documents
├── LICENSE                 # MIT License
└── README.md               # This file
```

## Usage

To use this site as a template for your own academic website:

1. **Go to the original repository**:  
   [https://github.com/olivineoverlord/olivineoverlord.github.io](https://github.com/olivineoverlord/olivineoverlord.github.io)

2. Click the **"Fork"** button in the top-right corner to create a copy of the repository under your own GitHub account.

3. After forking, go to **Settings** in your forked repository and **rename the repository** to:

   ```
   <your-github-username>.github.io
   ```

   > This is required for the site to publish to your GitHub Pages root URL.

4. **Clone your renamed repository** to your local machine:
   ```bash
   git clone https://github.com/<your-github-username>/<your-github-username>.github.io.git
   cd <your-github-username>.github.io
   ```

5. Modify the content:
   - Update HTML files like `index.html`, `about.html`, `research.html`, etc.
   - Add blog posts in the `blog/` directory
   - Replace images and documents in the `assets/` folder

6. **Deploy via GitHub Pages**:
   - Go to your repository’s **Settings** > **Pages**
   - Under "Source", choose the `main` branch (or the default branch)
   - Your website will be published at:
     `https://<your-github-username>.github.io/`

## Running Tests

To run the automated checks that verify blog post links, execute:

```bash
python3 -m unittest
```


## License

This project is released under the MIT License.  
You are welcome to adapt and reuse it. Attribution is appreciated but not required.

## Author

**Joshua Shea**  
Postdoctoral Researcher  
University of Cambridge  
[olivineoverlord.github.io/](https://olivineoverlord.github.io/)
