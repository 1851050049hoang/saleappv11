from saleapp import app, utils
from flask import render_template

@app.route("/")
def index():
    categories = utils.read_data()
    return render_template('index.html', categories=categories)

@app.route("/product")
def product_list():
    product_list = utils.read_data(path="data/products.json")
    return render_template('product.html', product_list = product_list)
if __name__ == "__main__":
    app.run(debug=True)