"""
Export Flask app into static HTML files for 100% GitHub Pages compatibility.
All links, assets, images, and routes will work directly on GitHub Pages!
"""

import os
import re
from app import app

# List of all routes and their output html file names
ROUTES = [
    ('/', 'index.html'),
    ('/interview', 'interview.html'),
    ('/resume', 'resume.html'),
    ('/dashboard', 'dashboard.html'),
    ('/skills', 'skills.html'),
    ('/role-matcher', 'role-matcher.html'),
    ('/projects', 'projects.html'),
    ('/about', 'about.html'),
    ('/certifications', 'certifications.html'),
    ('/achievements', 'achievements.html'),
    ('/contact', 'contact.html'),
    ('/profile', 'profile.html'),
]

def export_all():
    client = app.test_client()

    for route, filename in ROUTES:
        res = client.get(route)
        if res.status_code != 200:
            print(f"Error rendering {route}: Status {res.status_code}")
            continue

        html = res.data.decode('utf-8')

        # Convert absolute paths to relative paths for GitHub Pages subpath compatibility
        html = re.sub(r'href="/interview"', r'href="interview.html"', html)
        html = re.sub(r'href="/resume"', r'href="resume.html"', html)
        html = re.sub(r'href="/dashboard"', r'href="dashboard.html"', html)
        html = re.sub(r'href="/skills"', r'href="skills.html"', html)
        html = re.sub(r'href="/role-matcher"', r'href="role-matcher.html"', html)
        html = re.sub(r'href="/projects"', r'href="projects.html"', html)
        html = re.sub(r'href="/about"', r'href="about.html"', html)
        html = re.sub(r'href="/certifications"', r'href="certifications.html"', html)
        html = re.sub(r'href="/achievements"', r'href="achievements.html"', html)
        html = re.sub(r'href="/contact"', r'href="contact.html"', html)
        html = re.sub(r'href="/profile"', r'href="profile.html"', html)
        html = re.sub(r'href="/"', r'href="index.html"', html)
        
        # Convert static links to relative
        html = re.sub(r'/static/', r'static/', html)

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"[OK] Generated {filename}")

if __name__ == '__main__':
    export_all()
    print("\nAll static pages generated successfully for GitHub Pages!")
