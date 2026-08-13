"""
Verification Test Suite for CareerAI
Tests all 12 page routes and all REST API endpoints.
"""

import unittest
import json
from app import app
from database import init_db

class CareerAITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        with self.app.app_context():
            init_db()

    def test_all_page_routes(self):
        routes = [
            '/',
            '/interview',
            '/resume',
            '/dashboard',
            '/skills',
            '/role-matcher',
            '/projects',
            '/about',
            '/certifications',
            '/achievements',
            '/contact',
            '/profile'
        ]
        for route in routes:
            response = self.client.get(route)
            self.assertEqual(response.status_code, 200, f"Route {route} failed with status {response.status_code}")
            # Ensure developer name is present
            self.assertIn(b"Annareddy Naveen Kumar Reddy", response.data, f"Developer name missing in {route}")

    def test_api_status(self):
        res = self.client.get('/api/status')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data['status'], 'online')
        self.assertEqual(data['developer'], 'Annareddy Naveen Kumar Reddy')

    def test_interview_full_flow(self):
        # 1. Start Interview
        res = self.client.post('/api/interview/start', json={
            'role': 'Software Developer',
            'difficulty': 'Intermediate',
            'interview_type': 'Technical',
            'count': 3
        })
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertIn('interview_id', data)
        self.assertEqual(len(data['questions']), 3)
        interview_id = data['interview_id']

        # 2. Evaluate Question 1
        res = self.client.post('/api/interview/evaluate', json={
            'interview_id': interview_id,
            'question_number': 1,
            'question_text': data['questions'][0],
            'user_answer': 'In Python, memory management is handled by reference counting and garbage collection with cyclic isolation.',
            'role': 'Software Developer',
            'difficulty': 'Intermediate'
        })
        self.assertEqual(res.status_code, 200)
        eval_data = res.get_json()['evaluation']
        self.assertIn('overall_score', eval_data)
        self.assertIn('feedback_well', eval_data)
        self.assertIn('better_example', eval_data)

        # 3. Finish Interview
        res = self.client.post('/api/interview/finish', json={
            'interview_id': interview_id,
            'role': 'Software Developer',
            'difficulty': 'Intermediate'
        })
        self.assertEqual(res.status_code, 200)
        sum_data = res.get_json()['summary']
        self.assertIn('overall_score', sum_data)
        self.assertIn('readiness_rating', sum_data)

    def test_resume_analyzer(self):
        res = self.client.post('/api/resume/analyze-text', json={
            'text': 'Annareddy Naveen Kumar Reddy, ECE 3rd Year. Skills: Python, Flask, OpenCV, JavaScript, HTML5, CSS3, ESP32, IoT, SQLite, Git, GitHub.',
            'target_role': 'Software Developer'
        })
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertIn('ats_score', data)
        self.assertGreater(data['ats_score'], 50)
        self.assertIn('Python', data['detected_tech_skills'])

    def test_skill_gap_analysis(self):
        res = self.client.post('/api/skills/gap-analysis', json={
            'target_role': 'Software Developer'
        })
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertIn('skills_analyzed', data)
        self.assertGreater(len(data['skills_analyzed']), 0)

    def test_role_matcher(self):
        res = self.client.post('/api/role-matcher/match', json={
            'skills': ['python', 'flask', 'opencv', 'esp32', 'iot']
        })
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertIn('matches', data)
        self.assertGreater(len(data['matches']), 0)

    def test_contact_form(self):
        res = self.client.post('/contact', data={
            'name': 'Test Recruiter',
            'email': 'recruiter@techcompany.com',
            'message': 'We are impressed with your SmartLabTwinAI project and would like to invite you for an interview.'
        }, follow_redirects=True)
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"Thank you for reaching out", response_bytes := res.data)

if __name__ == '__main__':
    unittest.main()
