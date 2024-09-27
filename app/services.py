from datetime import datetime
from .models import db, Student, Achievement, StudentAchievement, Badge, StudentBadge

def calculate_leaderboard():
    students = Student.query.order_by(Student.points.desc()).limit(10).all()
    return [{'id': student.id, 'name': student.name, 'points': student.points} for student in students]

def award_achievement(student_id, achievement_id):
    achievement = Achievement.query.get(achievement_id)
    student = Student.query.get(student_id)
    if student and achievement:
        new_student_achievement = StudentAchievement(student_id=student.id, achievement_id=achievement.id, earned_date=datetime.now())
        student.points += achievement.points_required  # Add points to the student's score
        db.session.add(new_student_achievement)
        db.session.commit()

def award_badge(student_id, badge_id):
    badge = Badge.query.get(badge_id)
    student = Student.query.get(student_id)
    if student and badge:
        new_student_badge = StudentBadge(student_id=student.id, badge_id=badge.id, earned_date=datetime.now())
        db.session.add(new_student_badge)
        db.session.commit()
