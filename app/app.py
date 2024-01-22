from flask import Flask, request
from pick_regno import pick_regno


PICK_REGNO_MODEL_NAME = 'micromodel.cbm'


app = Flask(__name__)

@app.route('/pick_regno', methods=['GET'])
def regno_prediction():
    regno_recognize = request.args['regno_recognize']
    afts_regno_ai = request.args['afts_regno_ai']
    recognition_accuracy = request.args['recognition_accuracy']
    afts_regno_ai_score = request.args['afts_regno_ai_score']
    camera_type = request.args['camera_type']
    camera_class = request.args['camera_class']
    time_check = request.args['time_check']
    direction = request.args['direction']
    afts_regno_ai_score = request.args['afts_regno_ai_score']

    afts_regno_ai_char_scores = str(
        request.args.getlist('afts_regno_ai_char_scores')).replace(
        "'", '')
    afts_regno_ai_length_scores = str(
        request.args.getlist('afts_regno_ai_length_scores')).replace(
        "'", '')

    pick_regno_args = [regno_recognize, afts_regno_ai, recognition_accuracy, afts_regno_ai_score, afts_regno_ai_char_scores,
                    afts_regno_ai_length_scores, camera_type, camera_class, time_check, direction]

    if None in pick_regno_args:
        return "missing required parameters", 400

    predictions = pick_regno(*pick_regno_args, PICK_REGNO_MODEL_NAME)

    return {"class_0_probability": predictions[0],
            "class_1_probability": predictions[1]}, 200

if __name__ == "__main__":
    app.run()