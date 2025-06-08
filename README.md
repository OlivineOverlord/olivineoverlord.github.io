# [olivineoverlord.github.io/](https://olivineoverlord.github.io/)
## Personal Academic Website

This repository contains the source code for my personal academic website. It presents my research, publications, blog, academic profile, and contact details in a modern, responsive format designed for academic professionals.

## Design Philosophy

This site combines academic professionalism with modern web design. It features a clean, efficient CSS architecture with utility classes, automatic publication integration via ORCID API, and a responsive design that works seamlessly across devices. The focus is on showcasing research and facilitating academic collaboration.

## Key Features

### Academic Integration
- **Automatic publication display** via ORCID API integration
- **Harvard referencing format** with author name highlighting
- **Clickable publication cards** linking directly to papers
- **Dynamic blog integration** with latest post highlighting

### Modern Design
- **Utility-first CSS architecture** for maintainability
- **Responsive grid layouts** that adapt to any screen size
- **Professional card-based components** for content organization
- **Light/dark mode toggle** with system preference detection
- **Hover effects and animations** for enhanced user experience

### Performance & Accessibility
- **Efficient CSS** with minimal redundancy
- **Fast-loading** with optimized API calls
- **Semantic HTML** for accessibility
- **Mobile-first responsive design**
- **Cross-browser compatibility**

## Live Site

Visit the live site at: [olivineoverlord.github.io/](https://olivineoverlord.github.io/)

## File Structure

```
/
├── index.html              # Homepage with ORCID integration
├── about.html              # Academic background & CV
├── research.html           # Research projects & focus areas
├── blog.html               # Blog with dynamic post loading
├── contact.html            # Professional contact & collaboration
├── style/
│   └── style.css           # Efficient utility-based stylesheet
├── blog/
│   ├── posts.js            # Blog post data & logic
│   └── [post-files]/       # Individual blog posts
├── assets/
│   ├── images/             # Static images & graphics
│   └── documents/          # CV, papers, and documents
├── LICENSE                 # MIT License
└── README.md               # This file
```

## Technical Implementation

### CSS Architecture
The site uses an efficient utility-first CSS approach with:
- **Utility classes** (`.grid`, `.card`, `.center`, etc.) for rapid development
- **Component-specific styling** only where necessary
- **CSS custom properties** for theming and consistency
- **Responsive design** using CSS Grid and Flexbox

### ORCID API Integration
- **Automatic publication fetching** from ORCID profiles
- **Harvard citation formatting** with proper author attribution
- **Error handling** with graceful fallbacks
- **Performance optimization** with parallel API requests

### Blog System
- **JavaScript-driven** blog post rendering from JSON data
- **Automatic sorting** by publication date
- **Integration** with homepage highlights
- **Easy content management** through simple file updates

## Usage & Customization

To use this site as a template for your own academic website:

### 1. Fork & Setup
```bash
# Fork the repository on GitHub, then clone
git clone https://github.com/<your-username>/<your-username>.github.io.git
cd <your-username>.github.io
```

### 2. Customize Content
- **Update ORCID ID** in `index.html` (line with `ORCID_ID` variable)
- **Modify personal information** in all HTML files
- **Replace CV and documents** in `assets/documents/`
- **Update blog posts** in `blog/posts.js`

### 3. Styling Customization
The CSS uses custom properties for easy theming:
```css
:root {
  --bg: #fdfdfd;          /* Background color */
  --text: #222;           /* Text color */
  --accent: #2a4d69;      /* Accent/link color */
  --muted: #888;          /* Muted text color */
}
```

### 4. Deploy via GitHub Pages
- Repository Settings > Pages > Source: Main branch
- Site will be available at `https://<your-username>.github.io/`

## Key Components

### Publication Cards
Automatically generated from ORCID with:
- Harvard referencing format
- Author name highlighting
- Clickable links to papers
- Fallback to Google Scholar search

### Highlight Cards
Professional showcase cards featuring:
- Current research focus
- Recent recognition & awards
- Latest blog posts
- Collaboration opportunities

### Contact Integration
Streamlined contact options with:
- Professional email
- Academic profiles (ORCID, Google Scholar, ResearchGate)
- Social media presence

## Browser Compatibility
- **Modern browsers** (Chrome, Firefox, Safari, Edge)
- **Mobile responsive** design
- **Progressive enhancement** with graceful degradation

## Performance
- **Lightweight** CSS (~15KB optimized)
- **Fast API calls** with parallel processing
- **Optimized images** and assets
- **Minimal JavaScript** for core functionality

## License

This project is released under the MIT License. You are welcome to adapt and reuse it. Attribution is appreciated but not required.

## Contributing

Feel free to submit issues or pull requests for improvements. This template is designed to help other academics create professional web presences.

## Author

**Joshua Shea**  
Postdoctoral Researcher in Earth Sciences  
University of Cambridge  
[olivineoverlord.github.io/](https://olivineoverlord.github.io/)

---