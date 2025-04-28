# routes/journal.py

from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from models.entry import Entry
from extensions import db
from forms.entry_form import EntryForm
from datetime import datetime

journal_bp = Blueprint('journal', __name__)

# 📚 Dashboard
@journal_bp.route('/dashboard')
@login_required
def dashboard():
    total_entries = Entry.query.filter_by(user_id=current_user.id).count()
    
    now = datetime.utcnow()
    month_entries = Entry.query.filter(
        Entry.user_id == current_user.id,
        db.extract('year', Entry.date) == now.year,
        db.extract('month', Entry.date) == now.month
    ).count()

    recent_entries = Entry.query.filter_by(user_id=current_user.id).order_by(Entry.date.desc()).limit(5).all()

    return render_template('dashboard.html',
                           total_entries=total_entries,
                           month_entries=month_entries,
                           recent_entries=recent_entries)

# 📝 Create new entry
@journal_bp.route('/entry/new', methods=['GET', 'POST'])
@login_required
def new_entry():
    form = EntryForm()
    if form.validate_on_submit():
        entry = Entry(
            title=form.title.data,
            content=form.content.data,
            date=form.date.data or datetime.utcnow().date(),
            user_id=current_user.id
        )
        db.session.add(entry)
        db.session.commit()
        flash('Your journal entry has been created!', 'success')
        return redirect(url_for('journal.dashboard'))
    
    return render_template('create_entry.html', form=form, title='New Journal Entry')

# 📖 View entry
@journal_bp.route('/entry/<int:entry_id>')
@login_required
def view_entry(entry_id):
    entry = Entry.query.get_or_404(entry_id)
    if entry.user_id != current_user.id:
        flash('You do not have permission to view this entry.', 'danger')
        return redirect(url_for('journal.dashboard'))
    
    return render_template('view_entry.html', entry=entry)

# ✏️ Edit entry
@journal_bp.route('/entry/<int:entry_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_entry(entry_id):
    entry = Entry.query.get_or_404(entry_id)
    if entry.user_id != current_user.id:
        flash('You do not have permission to edit this entry.', 'danger')
        return redirect(url_for('journal.dashboard'))
    
    form = EntryForm(obj=entry)  # ⚡ pre-fill the form with the entry data

    if form.validate_on_submit():
        entry.title = form.title.data
        entry.content = form.content.data
        entry.date = form.date.data or entry.date
        entry.updated_at = datetime.utcnow()
        db.session.commit()
        flash('Your journal entry has been updated!', 'success')
        return redirect(url_for('journal.view_entry', entry_id=entry.id))

    return render_template('edit_entry.html', form=form, entry=entry, title='Edit Journal Entry')
    # ⚡ Now passing `entry=entry` to avoid Jinja2 error!

# 🗑️ Delete entry
@journal_bp.route('/entry/<int:entry_id>/delete', methods=['POST'])
@login_required
def delete_entry(entry_id):
    entry = Entry.query.get_or_404(entry_id)
    if entry.user_id != current_user.id:
        flash('You do not have permission to delete this entry.', 'danger')
        return redirect(url_for('journal.dashboard'))
    
    db.session.delete(entry)
    db.session.commit()
    flash('Your journal entry has been deleted.', 'success')
    return redirect(url_for('journal.dashboard'))

# 📅 Calendar View
@journal_bp.route('/calendar')
@login_required
def calendar():
    entries = Entry.query.filter_by(user_id=current_user.id).all()
    entry_dates = {}

    for entry in entries:
        date_str = entry.date.strftime('%Y-%m-%d')
        entry_info = {
            'id': entry.id,
            'title': entry.title,
            'content': entry.content,
            'created_at': entry.created_at.strftime('%Y-%m-%d %H:%M:%S'),
        }
        entry_dates.setdefault(date_str, []).append(entry_info)

    return render_template('calendar.html', entry_dates=entry_dates)

# 🔍 Search
@journal_bp.route('/search')
@login_required
def search():
    query = request.args.get('q', '').strip()
    if query:
        entries = Entry.query.filter(
            Entry.user_id == current_user.id,
            Entry.title.ilike(f'%{query}%')
        ).order_by(Entry.date.desc()).all()
    else:
        entries = []
    
    return render_template('search.html', entries=entries, query=query)
