from Vehicle.Vehicle import Vehicle
import scipy.integrate as integrate

class Analysis():
    

    def integrand(x):
        return x**4

    def calculate_p_r(start_time, end_time):
        res = 0

        res, err = integrate.quad(lambda x: x, start_time, end_time)
        res = res / (end_time - start_time)

        res = res * 0.9

        return res

    def M_P_R():
        pass

    def solution():
        p_r = calculate_p_r().. ...
        M-pr= M_P_R()..

        if(m-pr >= pr):
            average_charge = pr
        else:
            average_charge = m-pr

    





