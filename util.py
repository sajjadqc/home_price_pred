import pickle
__model = None
def load_saved_artifacts():

    print("Artifacts loading startes.....")

    global __model
    with open('./Artifacts/model.pickle', 'rb') as f:
        __model = pickle.load(f)


    print("artifacts loading completed.....")

def predict_home_price(size, total_sqft, bath):

    return __model.predict([[size, total_sqft, bath]])[0]

if __name__ == "__main__":
    load_saved_artifacts()
    print(predict_home_price(2, 1000, 3))
