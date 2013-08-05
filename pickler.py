import cPickle as pickle


def list_pickler(list, file):
    pickle.dump(list, file)


def unpickler(file):
    return pickle.load(file)
