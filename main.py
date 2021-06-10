from app import create_app
#yyyy
#app = create_app('fjhsdekufhnsdljkfhnsdkj lfhsdbnjkfshdbéfjk')

if __name__ == "__main__":
    app = create_app('fjhsdekufhnsdljkfhnsdkj lfhsdbnjkfshdbéfjk')
    app.run(debug=True,extra_files='./static/css/index.css')  