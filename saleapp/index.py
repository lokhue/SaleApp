from flask import Flask, render_template, request, redirect
import dao

app = Flask(__name__)


@app.route('/')
def index():
    q = request.args.get('q')
    cate_id = request.args.get('category_id')
    products = dao.load_products(q, cate_id)
    return render_template('index.html', products=products)


@app.route('/login', methods=['get', 'post'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'admin' and password == '12345678':
        return redirect('/')

    return render_template('login.html')


@app.route('/product/<int:id>')
def product_details(id):
    product = dao.load_product_by_id(id)
    return render_template('product-details.html', product=product)


@app.context_processor
def common_attributes():
    return {
        "categories": dao.load_categories()
    }


if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)