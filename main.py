from flask import Flask, request, render_template
import pickle

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home_page():
    return render_template('index.html')


@app.route('/prediction', methods=['POST'])
def predict_page():
    model = pickle.load(open('DecisionTreeClassifier.pickle', "rb"))

    workclass = {' Never-worked': 1, ' Without-pay': 2, ' ?': 3, ' Private': 4, ' State-gov': 5, ' Self-emp-not-inc': 6,
                 ' Local-gov': 7, ' Federal-gov': 8, ' Self-emp-inc': 9}
    education = {' Preschool': 1, ' 1st-4th': 2, ' 5th-6th': 3, ' 11th': 4, ' 9th': 5, ' 7th-8th': 6, ' 10th': 7,
                 ' 12th': 8, ' HS-grad': 9, ' Some-college': 10, ' Assoc-acdm': 11, ' Assoc-voc': 12, ' Bachelors': 13,
                 ' Masters': 14, ' Prof-school': 15, ' Doctorate': 16}
    marital_status = {' Never-married': 1, ' Separated': 2, ' Married-spouse-absent': 3, ' Widowed': 4, ' Divorced': 5,
                      ' Married-AF-spouse': 6, ' Married-civ-spouse': 7}
    occupation = {' Priv-house-serv': 1, ' Other-service': 2, ' Handlers-cleaners': 3, ' ?': 4, ' Armed-Forces': 5,
                  ' Farming-fishing': 6, ' Machine-op-inspct': 7, ' Adm-clerical': 8, ' Transport-moving': 9,
                  ' Craft-repair': 10, ' Sales': 11, ' Tech-support': 12, ' Protective-serv': 13, ' Prof-specialty': 14,
                  ' Exec-managerial': 15}
    relationship = {' Own-child': 1, ' Other-relative': 2, ' Unmarried': 3, ' Not-in-family': 4, ' Husband': 5,
                    ' Wife': 6}
    race = {' Other': 1, ' Amer-Indian-Eskimo': 2, ' Black': 3, ' White': 4, ' Asian-Pac-Islander': 5}
    sex = {' Female': 1, ' Male': 2}
    native_country = {' Holand-Netherlands': 1, ' Outlying-US(Guam-USVI-etc)': 2, ' Dominican-Republic': 3,
                      ' Columbia': 4, ' Guatemala': 5, ' Mexico': 6, ' Nicaragua': 7, ' Peru': 8, ' Vietnam': 9,
                      ' Honduras': 10, ' El-Salvador': 11, ' Haiti': 12, ' Puerto-Rico': 13, ' Trinadad&Tobago': 14,
                      ' Portugal': 15, ' Laos': 16, ' Jamaica': 17, ' Ecuador': 18, ' Thailand': 19, ' Poland': 20,
                      ' South': 21, ' Ireland': 22, ' Hungary': 23, ' United-States': 24, ' Scotland': 25, ' ?': 26,
                      ' Cuba': 27, ' China': 28, ' Greece': 29, ' Hong': 30, ' Philippines': 31, ' Germany': 32,
                      ' Canada': 33, ' England': 34, ' Italy': 35, ' Cambodia': 36, ' Yugoslavia': 37, ' Japan': 38,
                      ' Taiwan': 39, ' India': 40, ' France': 41, ' Iran': 42}

    if request.method == 'POST':
        user_input1 = float(request.form.get('input1'))
        user_input2 = workclass[str(request.form.get('input2'))]
        user_input3 = float(request.form.get('input3'))
        user_input4 = education[str(request.form.get('input4'))]
        user_input5 = marital_status[str(request.form.get('input5'))]
        user_input6 = occupation[str(request.form.get('input6'))]
        user_input7 = relationship[str(request.form.get('input7'))]
        user_input8 = race[str(request.form.get('input8'))]
        user_input9 = sex[str(request.form.get('input9'))]
        user_input10 = float(request.form.get('input10'))
        user_input11 = float(request.form.get('input11'))
        user_input12 = float(request.form.get('input12'))
        user_input13 = native_country[str(request.form.get('input13'))]
        prediction = model.predict(
            [[user_input1, user_input2, user_input3, user_input4, user_input5, user_input6,
              user_input7, user_input8, user_input9, user_input10, user_input11,
              user_input12, user_input13]])
        prediction = prediction[0]
        if prediction == 1:
            real_prediction = 'Yes his salary is more than 50 Inr'
        else:
            real_prediction = 'No his salary is not more than 50 Inr'

        return render_template("results.html", prediction=real_prediction)


if __name__ == '__main__':
    app.run(debug=True)
