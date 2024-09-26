from utils import ConverterUtils
from storage.base import BaseStorage



if __name__ == "__main__":
    var_cm = 100_000_000 # hanya untuk readable
    # var_cm_float = 100.000
    print(ConverterUtils.conver_cm_to_meter(var_cm))
    print(ConverterUtils.conver_cm_to_km(var_cm))
    storage = BaseStorage()
    print(storage)