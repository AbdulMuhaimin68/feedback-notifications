from flask import Blueprint, jsonify
from app.schemas.FeedbackSchema import FeedSchema
from app.repository.Feedback_Repo import Feedback_Repo
from webargs.flaskparser import use_args

bp = Blueprint('feedback', __name__)


@bp.route('/api/feedback', methods = ['POST'])
@use_args(FeedSchema(), location='json')
def add_feedback(args):
    session = Feedback_Repo.get_session()
    feedback = Feedback_Repo.add_mail(args, session = session)
    schema = FeedSchema()
    result = schema.dump(feedback)
    
    return jsonify({'result' : result})
