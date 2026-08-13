"""
AI Service Architecture for CareerAI.
Provides unified interface supporting Google Gemini, OpenAI, and high-fidelity Deterministic/Heuristic Demo Engine.
"""

import os
import json
import random
import re
from typing import Dict, Any, List
import requests
from config import Config
from services.mock_data import QUESTION_BANK, ROLE_TAXONOMY

class DemoEngine:
    """Intelligent fallback and demonstration engine providing realistic AI responses."""

    @staticmethod
    def get_questions(role: str, difficulty: str, interview_type: str, count: int = 5) -> List[str]:
        """Fetch realistic questions tailored to role, difficulty, and interview type."""
        role_data = QUESTION_BANK.get(role, QUESTION_BANK.get("Software Developer"))
        diff_data = role_data.get(difficulty, role_data.get("Intermediate"))
        type_questions = diff_data.get(interview_type, diff_data.get("Technical"))

        # Return questions up to requested count
        selected = list(type_questions)
        if len(selected) < count:
            # Supplement from mixed or other types
            for q in diff_data.get("Mixed", []):
                if q not in selected:
                    selected.append(q)
                if len(selected) >= count:
                    break
        return selected[:count]

    @staticmethod
    def evaluate_answer(role: str, difficulty: str, question: str, user_answer: str) -> Dict[str, Any]:
        """Dynamically evaluate a user's interview answer using heuristic NLP analysis."""
        clean_ans = user_answer.strip() if user_answer else ""
        word_count = len(re.findall(r'\w+', clean_ans))

        # Check if answer is minimal or empty
        if word_count < 5:
            return {
                "overall_score": 35,
                "technical_score": 30,
                "communication_score": 40,
                "confidence_score": 35,
                "relevance_score": 35,
                "answer_quality": 30,
                "feedback_well": "You attempted to respond, acknowledging the question prompt.",
                "feedback_missed": "The response is too brief to demonstrate technical depth, architectural understanding, or practical examples.",
                "feedback_improve": "Structure your answers using the STAR format (Situation, Task, Action, Result) or Definition + Architecture + Example framework.",
                "better_example": f"A comprehensive response would define the core concept, elaborate on its internal mechanism or trade-offs, and illustrate with a hands-on project scenario relevant to {role}."
            }

        # Calculate scores based on length, technical keywords, structure, and clarity
        tech_keywords = [
            "architecture", "performance", "optimization", "scalability", "complexity", "database", "api",
            "memory", "latency", "structure", "algorithm", "design", "security", "thread", "process",
            "asynchronous", "efficiency", "protocol", "framework", "component", "testing", "metric"
        ]
        
        matches = [kw for kw in tech_keywords if kw in clean_ans.lower()]
        keyword_density = min(len(matches), 6)

        # Baseline scoring
        base = 65
        if word_count >= 50:
            base += 10
        if word_count >= 100:
            base += 8
        if keyword_density >= 2:
            base += 7
        if keyword_density >= 4:
            base += 5

        # Difficulty adjustments
        if difficulty == "Advanced":
            base = max(40, base - 5)
        elif difficulty == "Beginner":
            base = min(96, base + 5)

        # Introduce small natural variance
        overall = min(96, max(45, base + random.randint(-3, 3)))
        tech = min(98, max(40, overall + (keyword_density * 2) - 2))
        comm = min(96, max(45, overall + (6 if word_count > 60 else -4)))
        conf = min(95, max(42, overall + random.randint(-4, 4)))
        relev = min(98, max(50, overall + random.randint(0, 4)))
        quality = int((tech * 0.4) + (comm * 0.3) + (relev * 0.3))

        # Dynamic feedback generation
        key_matched_str = ", ".join(matches[:3]) if matches else "foundational logic"
        
        feedback_well = f"Articulated fundamental concepts clearly with solid mention of {key_matched_str}. Good clarity of thought."
        feedback_missed = f"Could delve deeper into operational trade-offs, error handling scenarios, and performance implications under high load for {role}."
        feedback_improve = f"Use concrete numerical benchmarks or project examples (such as your work on IoT telemetry or computer vision) to substantiate technical assertions."

        # Context-aware better answer example
        better_example = (
            f"When answering '{question}', start with a direct 1-sentence definition: "
            f"Explain the underlying system architecture or mechanism, outline key advantages and trade-offs, "
            f"and conclude with how you applied this in a real-world scenario (e.g., handling edge cases, memory limits, or concurrency)."
        )

        return {
            "overall_score": overall,
            "technical_score": tech,
            "communication_score": comm,
            "confidence_score": conf,
            "relevance_score": relev,
            "answer_quality": quality,
            "feedback_well": feedback_well,
            "feedback_missed": feedback_missed,
            "feedback_improve": feedback_improve,
            "better_example": better_example
        }

    @staticmethod
    def generate_final_summary(role: str, difficulty: str, answers_data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Aggregate question scores into a comprehensive interview readiness summary."""
        if not answers_data:
            return {
                "overall_score": 75,
                "tech_score": 75,
                "comm_score": 75,
                "readiness_rating": "Placement Ready",
                "summary": "Completed mock interview session.",
                "strengths": ["Consistent participation", "Fundamental knowledge"],
                "weaknesses": ["Needs more in-depth architectural examples"],
                "recommended_topics": ["Data Structures", "System Design"]
            }

        avg_overall = int(sum(a.get("score", 70) for a in answers_data) / len(answers_data))
        avg_tech = int(sum(a.get("tech_score", 70) for a in answers_data) / len(answers_data))
        avg_comm = int(sum(a.get("comm_score", 70) for a in answers_data) / len(answers_data))
        avg_conf = int(sum(a.get("confidence_score", 70) for a in answers_data) / len(answers_data))
        avg_relev = int(sum(a.get("relevance_score", 70) for a in answers_data) / len(answers_data))

        # Readiness classification
        if avg_overall >= 85:
            rating = "Industry Placement Ready (High)"
        elif avg_overall >= 70:
            rating = "Placement Ready (Intermediate)"
        else:
            rating = "Needs Technical Refinement"

        role_info = ROLE_TAXONOMY.get(role, ROLE_TAXONOMY["Software Developer"])
        recommended_topics = role_info.get("interview_topics", ["Core Algorithms", "System Architecture", "API Design"])[:3]

        strengths = [
            f"Demonstrated solid grasp of {role} core concepts",
            "Structured communication with progressive clarity",
            "Confidence in handling standard and mixed scenario prompts"
        ]

        weaknesses = [
            "Can deepen technical depth around scalability and edge case handling",
            "Incorporate more quantitative impact metrics from academic/personal projects"
        ]

        summary = (
            f"Candidate completed a {difficulty} {role} interview evaluation with an overall score of {avg_overall}/100. "
            f"Technical proficiency scored {avg_tech}/100 and communication scored {avg_comm}/100. "
            f"Overall performance demonstrates readiness for competitive technical screenings."
        )

        return {
            "overall_score": avg_overall,
            "technical_score": avg_tech,
            "communication_score": avg_comm,
            "confidence_score": avg_conf,
            "relevance_score": avg_relev,
            "readiness_rating": rating,
            "summary": summary,
            "strengths": strengths,
            "weaknesses": weaknesses,
            "recommended_topics": recommended_topics
        }


class AIService:
    """Unified AI service coordinator with support for Gemini, OpenAI, and Demo Engine."""

    def __init__(self):
        self.provider = Config.AI_PROVIDER
        self.api_key = Config.AI_API_KEY
        self.model = Config.AI_MODEL

    def is_live_ai_available(self) -> bool:
        """Check if a valid third-party AI provider key is configured."""
        return bool(self.api_key and self.provider in ['gemini', 'openai'])

    def get_provider_name(self) -> str:
        """Return formatted name of active AI engine."""
        if self.is_live_ai_available():
            return f"Live AI ({self.provider.capitalize()})"
        return "CareerAI Demo Engine"

    def get_interview_questions(self, role: str, difficulty: str, interview_type: str, count: int = 5) -> List[str]:
        """Fetch or dynamically generate interview questions."""
        if not self.is_live_ai_available():
            return DemoEngine.get_questions(role, difficulty, interview_type, count)

        # Attempt Live AI Call if configured
        try:
            if self.provider == 'gemini':
                return self._gemini_generate_questions(role, difficulty, interview_type, count)
            elif self.provider == 'openai':
                return self._openai_generate_questions(role, difficulty, interview_type, count)
        except Exception as e:
            print(f"Error calling live AI API: {e}. Falling back to DemoEngine.")
        
        return DemoEngine.get_questions(role, difficulty, interview_type, count)

    def evaluate_interview_answer(self, role: str, difficulty: str, question: str, user_answer: str) -> Dict[str, Any]:
        """Evaluate a single interview answer."""
        if not self.is_live_ai_available():
            return DemoEngine.evaluate_answer(role, difficulty, question, user_answer)

        try:
            if self.provider == 'gemini':
                return self._gemini_evaluate_answer(role, difficulty, question, user_answer)
            elif self.provider == 'openai':
                return self._openai_evaluate_answer(role, difficulty, question, user_answer)
        except Exception as e:
            print(f"Error in Live AI evaluation: {e}. Falling back to DemoEngine.")

        return DemoEngine.evaluate_answer(role, difficulty, question, user_answer)

    def summarize_interview(self, role: str, difficulty: str, answers_data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Generate final interview report and readiness score."""
        return DemoEngine.generate_final_summary(role, difficulty, answers_data)

    def _gemini_generate_questions(self, role: str, difficulty: str, interview_type: str, count: int) -> List[str]:
        """Generate questions using Google Gemini API."""
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{self.model}:generateContent?key={self.api_key}"
        prompt = (
            f"Generate exactly {count} professional interview questions for a {difficulty}-level {role} position. "
            f"Interview Type: {interview_type}. "
            f"Return the response as a JSON array of strings ONLY. No markdown formatting, no other text."
        )
        payload = {"contents": [{"parts": [{"text": prompt}]}]}
        res = requests.post(url, json=payload, timeout=10)
        res.raise_for_status()
        data = res.json()
        text = data['candidates'][0]['content']['parts'][0]['text'].strip()
        # Clean JSON markdown if any
        text = re.sub(r'^```json\s*', '', text)
        text = re.sub(r'\s*```$', '', text)
        questions = json.loads(text)
        if isinstance(questions, list) and len(questions) > 0:
            return questions[:count]
        return DemoEngine.get_questions(role, difficulty, interview_type, count)

    def _openai_generate_questions(self, role: str, difficulty: str, interview_type: str, count: int) -> List[str]:
        """Generate questions using OpenAI API."""
        url = "https://api.openai.com/v1/chat/completions"
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
        prompt = (
            f"Generate exactly {count} professional interview questions for a {difficulty}-level {role} position. "
            f"Interview Type: {interview_type}. "
            f"Return ONLY a JSON array of strings."
        )
        payload = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7
        }
        res = requests.post(url, headers=headers, json=payload, timeout=10)
        res.raise_for_status()
        data = res.json()
        text = data['choices'][0]['message']['content'].strip()
        text = re.sub(r'^```json\s*', '', text)
        text = re.sub(r'\s*```$', '', text)
        questions = json.loads(text)
        if isinstance(questions, list) and len(questions) > 0:
            return questions[:count]
        return DemoEngine.get_questions(role, difficulty, interview_type, count)

    def _gemini_evaluate_answer(self, role: str, difficulty: str, question: str, user_answer: str) -> Dict[str, Any]:
        """Evaluate answer using Gemini."""
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{self.model}:generateContent?key={self.api_key}"
        prompt = (
            f"Evaluate this interview answer for a {difficulty} {role}.\n"
            f"Question: {question}\n"
            f"Answer: {user_answer}\n\n"
            f"Provide output as a valid JSON object with the following keys:\n"
            f"- overall_score (integer 0-100)\n"
            f"- technical_score (integer 0-100)\n"
            f"- communication_score (integer 0-100)\n"
            f"- confidence_score (integer 0-100)\n"
            f"- relevance_score (integer 0-100)\n"
            f"- answer_quality (integer 0-100)\n"
            f"- feedback_well (concise string)\n"
            f"- feedback_missed (concise string)\n"
            f"- feedback_improve (actionable tip string)\n"
            f"- better_example (model answer string)\n"
            f"Return JSON only."
        )
        payload = {"contents": [{"parts": [{"text": prompt}]}]}
        res = requests.post(url, json=payload, timeout=12)
        res.raise_for_status()
        data = res.json()
        text = data['candidates'][0]['content']['parts'][0]['text'].strip()
        text = re.sub(r'^```json\s*', '', text)
        text = re.sub(r'\s*```$', '', text)
        return json.loads(text)

    def _openai_evaluate_answer(self, role: str, difficulty: str, question: str, user_answer: str) -> Dict[str, Any]:
        """Evaluate answer using OpenAI."""
        url = "https://api.openai.com/v1/chat/completions"
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
        prompt = (
            f"Evaluate this interview answer for a {difficulty} {role}.\n"
            f"Question: {question}\n"
            f"Answer: {user_answer}\n\n"
            f"Return ONLY a JSON object with keys: overall_score, technical_score, communication_score, "
            f"confidence_score, relevance_score, answer_quality, feedback_well, feedback_missed, "
            f"feedback_improve, better_example."
        )
        payload = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.5
        }
        res = requests.post(url, headers=headers, json=payload, timeout=12)
        res.raise_for_status()
        data = res.json()
        text = data['choices'][0]['message']['content'].strip()
        text = re.sub(r'^```json\s*', '', text)
        text = re.sub(r'\s*```$', '', text)
        return json.loads(text)

# Singleton instance
ai_service = AIService()
