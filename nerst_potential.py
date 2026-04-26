import math

def nernst_potential(cin, cout, z, t):
    """
    Computes Nernst potential at specified temperature.

    Args:
        cin (float): Internal ionic concentration.
        cout (float): External ionic concentration.
        z (float): Ion valence (with sign).
        t (float): Temperature in degrees Celsius.

    Returns:
        float: Nernst potential in mV.

    Notes:
        - Cin and Cout need to be in the same units.
        - The standard formula for Nernst potential is:
          E = (RT/zF) * ln([C_in]/[C_out])
          Where:
            R = 8.314 J/(mol*K) (Ideal gas constant)
            T_kelvin = T_celsius + 273.15 (Temperature in Kelvin)
            F = 96485 C/mol (Faraday constant)
            z = ion valence
            [C] = concentration
    """
    # Convert temperature from Celsius to Kelvin
    t_kelvin = t + 273.15

    # Constants
    k = 1.38 * 10**(-23)

    # Calculate the Nernst potential using the formula derived from thermodynamics:
    # E = (RT / zF) * ln(C_in / C_out)
    try:
        term1 = k * t_kelvin / (z * 1.6 * 10**(-19))
        ratio = cin / cout
        e = term1 * math.log(ratio)
    except ZeroDivisionError:
        print("Error: Ion valence (z) cannot be zero.")
        return float('nan')
    except ValueError:
        # This might happen if ratio is negative, which shouldn't occur with concentrations
        print("Error: Concentration ratio resulted in an invalid logarithm argument.")
        return float('nan')

    # The result from the formula above will be in Volts (V) because R and F units cancel out appropriately.
    # Since the desired output is in mV, we multiply by 1000.
    e_mv = e * 1000

    return e_mv

# Example Usage:
C_in = 4.8  # Molar concentration inside
C_out = 186 # Molar concentration outside
z_val = 1   # Valence (e.g., for Mg^2+)
T_celsius = 37 # Temperature in Celsius

nernst_potential_mv = nernst_potential(C_in, C_out, z_val, T_celsius)

if not math.isnan(nernst_potential_mv):
    print("\n" + "="*30)
    print(f"Internal Concentration (Cin): {C_in}")
    print(f"External Concentration (Cout): {C_out}")
    print(f"Ion Valence (z): {z_val}")
    print(f"Temperature: {T_celsius}°C")
    print(f"\nCalculated Nernst Potential for K+ Ions (E): {nernst_potential_mv:.2f} mV")

