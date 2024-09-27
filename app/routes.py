from flask import Blueprint, request, jsonify
from .models import db, Student, Course, Lesson, Achievement, Badge
from .services import calculate_leaderboard, award_achievement, award_badge

main = Blueprint('main', __name__)

@main.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([{'id': student.id, 'name': student.name, 'points': student.points} for student in students])

@main.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = Student.query.get_or_404(id)
    return jsonify({'id': student.id, 'name': student.name, 'points': student.points})

@main.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    new_student = Student(name=data['name'], email=data['email'])
    db.session.add(new_student)
    db.session.commit()
    return jsonify({'message': 'Student added successfully'}), 201

@main.route('/courses', methods=['GET'])
def get_courses():
    courses = Course.query.all()
    return jsonify([{'id': course.id, 'name': course.name} for course in courses])

@main.route('/leaderboard', methods=['GET'])
def leaderboard():
    leaderboard_data = calculate_leaderboard()
    return jsonify(leaderboard_data)

@main.route('/award-achievement', methods=['POST'])
def award_achievement_route():
    data = request.get_json()
    award_achievement(student_id=data['student_id'], achievement_id=data['achievement_id'])
    return jsonify({'message': 'Achievement awarded successfully'})

@main.route('/award-badge', methods=['POST'])
def award_badge_route():
    data = request.get_json()
    award_badge(student_id=data['student_id'], badge_id=data['badge_id'])
    return jsonify({'message': 'Badge awarded successfully'})
