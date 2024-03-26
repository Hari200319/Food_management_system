from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data structure to store NGO information
ngos = []

@app.route('/')
def index():
    return render_template('sample.html')

@app.route('/add_ngo', methods=['GET', 'POST'])
def add_ngo():
    if request.method == 'POST':
        # Retrieve data from the form
        ngo_name = request.form['ngo_name']
        location = request.form['location']
        contact_person = request.form['contact_person']
        contact_email = request.form['contact_email']
        contact_phone = request.form['contact_phone']
        
        # Store the NGO data in the ngos list (or you can store it in a database)
        ngos.append({
            'ngo_name': ngo_name,
            'location': location,
            'contact_person': contact_person,
            'contact_email': contact_email,
            'contact_phone': contact_phone
        })
        
        # Redirect to the homepage or any other appropriate page
        return redirect(url_for('index'))
    
    return render_template('add_ngo_form.html')

@app.route('/view_ngos')
def view_ngos():
    return render_template('view_ngos.html', ngos=ngos)

if __name__ == '__main__':
    app.run(debug=True)
