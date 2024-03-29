import numpy as np  # type: ignore
import matplotlib.pyplot as plt  # type: ignore
# from readVDF_2_new_files import *  # type: ignore
from readVDF2 import Plt  # type: ignore

# Switches ---------------------------------------------------------
test = 0
test2 = 0
A = 0
B = 0
Gamma_on = 1
Beta_on = 0

# Figures ---------------------------------------------------------------------
# WF: Works For
Fig2a_vr_vPhi_vTheta_divided_by_gauss = 0  # WF: test, test2
Fig2b_vt_divided_by_gauss = 0  # WF: test, test2
Fig3a_GPerts_same_gammas_as_IC_vr = 0  # WF: test. test2?
Fig3b_GPerts_G1_2_same_gammas_as_IC_vt = 0  # Not yet created
Fig4_GPerts_different_gammas_vt = 0  # WF: test, test2, B
# Next 4 figures works for test, test2, B:
Fig5a_GPerts_gammas_1_5_vt_divided_by_gauss_and_Tsallis = 0
Fig5b_GPerts_gammas_2_0_vt_divided_by_gauss_and_Tsallis = 0
Fig5c_GPerts_gammas_2_5_vt_divided_by_gauss_and_Tsallis = 0
Fig5d_GPerts_gammas_3_0_vt_divided_by_gauss_and_Tsallis = 0
# Next 2 figures works for A, B:
Fig6a_GPerts_R_middle_19_95_vt_divided_by_gauss_and_Tsallis = 0
Fig6b_GPerts_R_middle_31_62_vt_divided_by_gauss_and_Tsallis = 0

if Fig2a_vr_vPhi_vTheta_divided_by_gauss:
    f, (ax1, ax2) = plt.subplots(1, 2)
    ax1.set_xlabel(r"$u_r$, $u_{\Theta}$ and $u_{\Phi}$", fontsize=20)
    ax1.set_ylabel(r"$\frac{f\left(u \right)}{ae^{-bx^2}}$", fontsize=20)
    ax2.set_xlabel(
        r"$\log \left( |u_rn|,u_rp \right)$, $\log \left(\
                   |u_{\Theta}n|,u_{\Theta}p \right)$ and $\log \left(\
                   |u_{\Phi}n|,u_{\Phi}p \right)$",
        fontsize=20,
    )
    ax2.set_ylabel(
        r"$\frac{f\left(\log \left( |u_n|,\
                   u_p \right)\right)}{axe^{-b\log (x)^2}}$",
        fontsize=20,
    )

    if test:
        for i in range(1, 3):
            exec(f"ax{i}.grid()")

        for i in range(1, 3):
            exec(
                f"ax{i}.legend(prop=dict(size=13), numpoints=2, ncol=1,\
                                frameon=True, loc=0, handlelength=2.5)"
            )

        def denom_ax1(a, b, c):
            return a * np.exp(b * c**2)

        d, _ = bin2_HQ10000_G1_2_1_005[1]
        ax1.plot(
            d[:, 0],
            d[:, 1] / denom_ax1(478.006, -0.456, d[:, 0]),
            "g:",
            label=r"$r, a=478.006, b=0.456$",
            lw=4,
            ms=7,
        )
        d, _ = bin2_HQ10000_G1_2_1_005[2]
        ax1.plot(
            d[:, 0],
            d[:, 1] / denom_ax1(482.605, -0.473, d[:, 0]),
            "r:",
            label=r"$\Theta, a=482.605, b=0.473$",
            lw=4,
            ms=7,
        )
        d, _ = bin2_HQ10000_G1_2_1_005[3]
        ax1.plot(
            d[:, 0],
            d[:, 1] / denom_ax1(502.652, -0.477, d[:, 0]),
            "k:",
            label=r"$\Phi, a=502.652, b=0.477$",
            lw=2,
            ms=7,
        )
        ax1.set_title(r"File = %s, $\gamma = -2.0$" % HQ12, fontsize=20)

        d, _ = bin2_HQ10000_G1_2_1_005[5]
        ax2.plot(
            d[:, 0],
            d[:, 1]
            / (1433.228 * 10 ** d[:, 0] * np.exp(-0.472 * (10 ** d[:, 0]) ** 2)),
            "g:",
            label=r"$a=1433.228, b=0.472$",
            lw=2,
            ms=7,
        )
        d, _ = bin2_HQ10000_G1_2_1_005[6]
        ax2.plot(
            d[:, 0],
            d[:, 1]
            / (1416.346 * 10 ** d[:, 0] * np.exp(-0.473 * (10 ** d[:, 0]) ** 2)),
            "r:",
            label=r"$ a=1416.346, b=0.473 $",
            lw=2,
            ms=7,
        )
        d, _ = bin2_HQ10000_G1_2_1_005[7]
        ax2.plot(
            d[:, 0],
            d[:, 1]
            / (1405.914 * 10 ** d[:, 0] * np.exp(-0.470 * (10 ** d[:, 0]) ** 2)),
            "k:",
            label=r"$a=1405.914, b=0.470$",
            lw=2,
            ms=7,
        )

    if test2:
        for i in range(1, 3):
            exec(f"ax{i}.grid()")

        for i in range(1, 3):
            exec(
                f"ax{i}.legend(prop=dict(size=13), numpoints=2, ncol=1,\
                                frameon=True, loc=0, handlelength=2.5)"
            )

        d, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[1]
        ax1.plot(
            d[:, 0],
            d[:, 1] / (478.006 * np.exp(-0.456 * d[:, 0] ** 2)),
            "g:",
            label=r"$r, a=478.006, b=0.456$",
            lw=4,
            ms=7,
        )
        d, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[2]
        ax1.plot(
            d[:, 0],
            d[:, 1] / (482.605 * np.exp(-0.473 * d[:, 0] ** 2)),
            "r:",
            label=r"$\Theta, a=482.605, b=0.473$",
            lw=4,
            ms=7,
        )
        d, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[3]
        ax1.plot(
            d[:, 0],
            d[:, 1] / (502.652 * np.exp(-0.477 * d[:, 0] ** 2)),
            "k:",
            label=r"$\Phi, a=502.652, b=0.477$",
            lw=2,
            ms=7,
        )
        ax1.set_xlabel(r"$u_r$, $u_{\Theta}$ and $u_{\Phi}$", fontsize=20)
        ax1.set_ylabel(r"$\frac{f\left(u \right)}{ae^{-bx^2}}$", fontsize=20)
        ax1.set_title(r"File = %s, $\gamma = -2.0$" % test2_HQ0, fontsize=20)

        d, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[5]
        ax2.plot(
            d[:, 0],
            d[:, 1]
            / (1433.228 * 10 ** d[:, 0] * np.exp(-0.472 * (10 ** d[:, 0]) ** 2)),
            "g:",
            label=r"$a=1433.228, b=0.472$",
            lw=2,
            ms=7,
        )
        d, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[6]
        ax2.plot(
            d[:, 0],
            d[:, 1]
            / (1416.346 * 10 ** d[:, 0] * np.exp(-0.473 * (10 ** d[:, 0]) ** 2)),
            "r:",
            label=r"$a=1416.346, b=0.473$",
            lw=2,
            ms=7,
        )
        d, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[7]
        ax2.plot(
            d[:, 0],
            d[:, 1]
            / (1405.914 * 10 ** d[:, 0] * np.exp(-0.470 * (10 ** d[:, 0]) ** 2)),
            "k:",
            label=r"$ a=1405.914, b=0.470$",
            lw=2,
            ms=7,
        )

if Fig2b_vt_divided_by_gauss:
    f, (ax1, ax2) = plt.subplots(1, 2)

    for i in range(1, 3):
        exec(f"ax{i}.grid()")

    def denom_ax1(a):
        return 918.083 * a * np.exp(-0.922 * a**2)

    def denom_ax2(a):
        return 3400.442 * (10**a) ** 2 * np.exp(-0.930 * (10**a) ** 2)

    ax1.set_ylim(0, 2)
    ax1.set_xlabel(r"$u_t$", fontsize=20)
    ax1.set_ylabel(r"$\frac{f\left(u_t \right)}{918.083xe^{-0.922x^2}}$", fontsize=20)
    ax1.legend(
        prop=dict(size=13), numpoints=2, ncol=1, frameon=True, loc=0, handlelength=2.5
    )
    ax2.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
    ax2.set_ylabel(
        r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}\
                   {3400.442x^2e^{-0.930x^2}}$",
        fontsize=20,
    )

    if test:
        d, _ = bin1_HQ10000_G1_2_1_005[0]
        ax1.plot(
            d[:, 0], d[:, 1] / denom_ax1(d[:, 0]), "b--", label=r"$\gamma = -1.5$", lw=3
        )
        d, _ = bin2_HQ10000_G1_2_1_005[0]
        ax1.plot(
            d[:, 0],
            d[:, 1] / denom_ax1(d[:, 0]),
            "b:",
            label=r"$\gamma = -2.0$",
            lw=4,
            ms=7,
        )
        d, _ = bin3_HQ10000_G1_2_1_005[0]
        ax1.plot(
            d[:, 0],
            d[:, 1] / denom_ax1(d[:, 0]),
            "b-.",
            label=r"$\gamma = -2.5$",
            lw=4,
            ms=7,
        )
        d, _ = bin4_HQ10000_G1_2_1_005[0]
        ax1.plot(
            d[:, 0],
            d[:, 1] / denom_ax1(d[:, 0]),
            "b",
            label=r"$\gamma = -3.0$",
            lw=2,
            ms=7,
        )
        ax1.set_title("File = %s" % HQ12, fontsize=20)

        d, _ = bin1_HQ10000_G1_2_1_005[4]
        ax2.plot(
            d[:, 0],
            d[:, 1] / denom_ax2(d[:, 0]),
            "b--",
            label=r"$\gamma = -1.5$",
            lw=2,
            ms=7,
        )
        d, _ = bin2_HQ10000_G1_2_1_005[4]
        ax2.plot(
            d[:, 0],
            d[:, 1] / denom_ax2(d[:, 0]),
            "b:",
            label=r"$\gamma = -2.0$",
            lw=2,
            ms=7,
        )
        d, _ = bin3_HQ10000_G1_2_1_005[4]
        ax2.plot(
            d[:, 0],
            d[:, 1] / denom_ax2(d[:, 0]),
            "b-.",
            label=r"$\gamma = -2.5$",
            lw=2,
            ms=7,
        )
        d, _ = bin4_HQ10000_G1_2_1_005[4]
        ax2.plot(
            d[:, 0],
            d[:, 1] / denom_ax2(d[:, 0]),
            "b",
            label=r"$\gamma = -3.0$",
            lw=2,
            ms=7,
        )

    if test2:
        d, _ = bin1_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(
            d[:, 0], d[:, 1] / denom_ax1(d[:, 0]), "b--", label=r"$\gamma = -1.5$", lw=3
        )
        d, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(
            d[:, 0],
            d[:, 1] / denom_ax1(d[:, 0]),
            "b:",
            label=r"$\gamma = -2.0$",
            lw=4,
            ms=7,
        )
        d, _ = bin3_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(
            d[:, 0],
            d[:, 1] / denom_ax1(d[:, 0]),
            "b-.",
            label=r"$\gamma = -2.5$",
            lw=4,
            ms=7,
        )
        d, _ = bin4_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax1.plot(
            d[:, 0],
            d[:, 1] / denom_ax1(d[:, 0]),
            "b",
            label=r"$\gamma = -3.0$",
            lw=2,
            ms=7,
        )
        ax1.set_title("File = %s" % test2_HQ0, fontsize=20)

        d, _ = bin1_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(
            d[:, 0],
            d[:, 1] / denom_ax2(d[:, 0]),
            "b--",
            label=r"$\gamma = -1.5$",
            lw=2,
            ms=7,
        )
        d, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(
            d[:, 0],
            d[:, 1] / denom_ax2(d[:, 0]),
            "b:",
            label=r"$\gamma = -2.0$",
            lw=2,
            ms=7,
        )
        d, _ = bin3_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(
            d[:, 0],
            d[:, 1] / denom_ax2(d[:, 0]),
            "b-.",
            label=r"$\gamma = -2.5$",
            lw=2,
            ms=7,
        )
        d, _ = bin4_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax2.plot(
            d[:, 0],
            d[:, 1] / denom_ax2(d[:, 0]),
            "b",
            label=r"$\gamma = -3.0$",
            lw=2,
            ms=7,
        )

if Fig3a_GPerts_same_gammas_as_IC_vr:
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

    for i in range(1, 5):
        exec(f"ax{i}.grid()")

    for i in range(1, 5):
        exec(
            f"ax{i}.legend(prop=dict(size=13), numpoints=2, ncol=1,\
                            frameon=True, loc=0, handlelength=2.5)"
        )

    Plt(1, bin1_HQ10000_G1_0_0_000[0], "b--", HQ0[9:])
    data, _ = bin1_HQ10000_G1_0_0_000[1]
    ax1.plot(data[:, 0], data[:, 1], "Skyblue", ls="--", lw=2, ms=7)
    Plt(1, bin1_HQ10000_G1_2_1_005[0], "r--", HQ12[9:])
    data, _ = bin1_HQ10000_G1_2_1_005[1]
    ax1.plot(data[:, 0], data[:, 1], "Pink", ls="--", lw=2, ms=7)
    Plt(1, bin1_HQ10000_G0_8_2_005[0], "g--", HQ18[9:])
    data, _ = bin1_HQ10000_G0_8_2_005[1]
    ax1.plot(data[:, 0], data[:, 1], "Chartreuse", ls="--", lw=2, ms=7)
    Plt(1, bin1_HQ10000_G1_2_5_005[0], "k--", HQ36[9:])
    data, _ = bin1_HQ10000_G1_2_5_005[1]
    ax1.plot(data[:, 0], data[:, 1], "Brown", ls="--", lw=2, ms=7)
    data, _ = bin1_HQ10000_G1_2_9_005[0]
    ax1.plot(data[:, 0], data[:, 1], "Orange", HQ60[9:], ls="--", lw=2, ms=7)
    Plt(1, bin1_HQ10000_G1_2_9_005[1], "y--")
    Plt(1, bin1_HQ10000_G1_0_10_009[0], HQ70[9:], "m--")
    Plt(1, bin1_HQ10000_G1_0_10_009[1], "c--")
    Plt(1, bin2_HQ10000_G1_0_0_000[0], "b:")  # label=r'$\gamma = -2.0$'
    data, _ = bin2_HQ10000_G1_0_0_000[1]
    ax1.plot(data[:, 0], data[:, 1], "Skyblue", ls=":", lw=4, ms=7)
    Plt(1, bin2_HQ10000_G1_2_1_005[0], "r:")
    data, _ = bin2_HQ10000_G1_2_1_005[1]
    ax1.plot(data[:, 0], data[:, 1], "Pink", ls=":", lw=4, ms=7)
    Plt(1, bin2_HQ10000_G0_8_2_005[0], "g:")
    data, _ = bin2_HQ10000_G0_8_2_005[1]
    ax1.plot(data[:, 0], data[:, 1], "Chartreuse", ls=":", lw=4, ms=7)
    Plt(1, bin2_HQ10000_G1_2_5_005[0], "k:")
    data, _ = bin2_HQ10000_G1_2_5_005[1]
    ax1.plot(data[:, 0], data[:, 1], "Brown", ls=":", lw=4, ms=7)
    data, _ = bin2_HQ10000_G1_2_9_005[0]
    ax1.plot(data[:, 0], data[:, 1], "Orange", ls=":", lw=4, ms=7)
    Plt(1, bin2_HQ10000_G1_2_9_005[1], "y:")
    Plt(1, bin2_HQ10000_G1_0_10_009[0], "m:")
    Plt(1, bin2_HQ10000_G1_0_10_009[1], "c:")
    Plt(1, bin3_HQ10000_G1_0_0_000[0], "b-.")  # label=r'$\gamma = -2.5$'
    data, _ = bin3_HQ10000_G1_0_0_000[1]
    ax1.plot(data[:, 0], data[:, 1], "Skyblue", ls="-.", lw=4, ms=7)
    Plt(1, bin3_HQ10000_G1_2_1_005[0], "r-.")
    data, _ = bin3_HQ10000_G1_2_1_005[1]
    ax1.plot(data[:, 0], data[:, 1], "Pink", ls="-.", lw=4, ms=7)
    Plt(1, bin3_HQ10000_G0_8_2_005[0], "g-.")
    data, _ = bin3_HQ10000_G0_8_2_005[1]
    ax1.plot(data[:, 0], data[:, 1], "Chartreuse", ls="-.", lw=4, ms=7)
    Plt(1, bin3_HQ10000_G1_2_5_005[0], "k-.")
    data, _ = bin3_HQ10000_G1_2_5_005[1]
    ax1.plot(data[:, 0], data[:, 1], "Brown", ls="-.", lw=4, ms=7)
    data, _ = bin3_HQ10000_G1_2_9_005[0]
    ax1.plot(data[:, 0], data[:, 1], "Orange", ls="-.", lw=4, ms=7)
    Plt(1, bin3_HQ10000_G1_2_9_005[1], "y-.")
    Plt(1, bin3_HQ10000_G1_0_10_009[0], "m-.")
    Plt(1, bin3_HQ10000_G1_0_10_009[1], "c-.")
    Plt(1, bin4_HQ10000_G1_0_0_000[0], "b")  # label=r'$\gamma = -3.0$'
    data, _ = bin4_HQ10000_G1_0_0_000[1]
    ax1.plot(data[:, 0], data[:, 1], "Skyblue", lw=2, ms=7)
    Plt(1, bin4_HQ10000_G1_2_1_005[0], "r")
    data, _ = bin4_HQ10000_G1_2_1_005[1]
    ax1.plot(data[:, 0], data[:, 1], "Pink", lw=2, ms=7)
    Plt(1, bin4_HQ10000_G0_8_2_005[0], "g")
    data, _ = bin4_HQ10000_G0_8_2_005[1]
    ax1.plot(data[:, 0], data[:, 1], "Chartreuse", lw=2, ms=7)
    Plt(1, bin4_HQ10000_G1_2_5_005[0], "k")
    data, _ = bin4_HQ10000_G1_2_5_005[1]
    ax1.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
    data, _ = bin4_HQ10000_G1_2_9_005[0]
    ax1.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
    Plt(1, bin4_HQ10000_G1_2_9_005[1], "y")
    Plt(1, bin4_HQ10000_G1_0_10_009[0], "m")
    Plt(1, bin4_HQ10000_G1_0_10_009[1], "c")

    ax1.set_xlabel(r"$u_t$ and $u_r$", fontsize=20)
    ax1.set_ylabel(r"$f\left(u\right)$", fontsize=20)
    ax1.set_title("Time evolution of files = %s" % HQ0[:-9], fontsize=20)

    # label=r'$\gamma = -1.5$'
    Plt(2, bin1_HQ10000_G1_0_0_000[4], "b--", HQ0[9:])
    data, _ = bin1_HQ10000_G1_0_0_000[5]
    ax2.plot(data[:, 0], data[:, 1], "Skyblue", ls="--", lw=2, ms=7)
    Plt(2, bin1_HQ10000_G1_2_1_005[4], "r--", HQ12[9:])
    data, _ = bin1_HQ10000_G1_2_1_005[5]
    ax2.plot(data[:, 0], data[:, 1], "Pink", ls="--", lw=2, ms=7)
    Plt(2, bin1_HQ10000_G0_8_2_005[4], "g--", HQ18[9:])
    data, _ = bin1_HQ10000_G0_8_2_005[5]
    ax2.plot(data[:, 0], data[:, 1], "Chartreuse", ls="--", lw=2, ms=7)
    Plt(2, bin1_HQ10000_G1_2_5_005[4], "k--", HQ36[9:])
    data, _ = bin1_HQ10000_G1_2_5_005[5]
    ax2.plot(data[:, 0], data[:, 1], "Brown", ls="--", lw=2, ms=7)
    data, _ = bin1_HQ10000_G1_2_9_005[4]
    ax2.plot(data[:, 0], data[:, 1], "Orange", HQ60[9:], ls="--", lw=2, ms=7)
    Plt(2, bin1_HQ10000_G1_2_9_005[5], "y--")
    Plt(2, bin1_HQ10000_G1_0_10_009[4], HQ70[9:], "m--")
    Plt(2, bin1_HQ10000_G1_0_10_009[5], "c--")
    Plt(2, bin2_HQ10000_G1_0_0_000[4], "b:")  # label=r'$\gamma = -2.0$'
    data, _ = bin2_HQ10000_G1_0_0_000[5]
    ax2.plot(data[:, 0], data[:, 1], "Skyblue", ls=":", lw=2, ms=7)
    Plt(2, bin2_HQ10000_G1_2_1_005[4], "r:")
    data, _ = bin2_HQ10000_G1_2_1_005[5]
    ax2.plot(data[:, 0], data[:, 1], "Pink", ls=":", lw=2, ms=7)
    Plt(2, bin2_HQ10000_G0_8_2_005[4], "g:")
    data, _ = bin2_HQ10000_G0_8_2_005[5]
    ax2.plot(data[:, 0], data[:, 1], "Chartreuse", ls=":", lw=2, ms=7)
    Plt(2, bin2_HQ10000_G1_2_5_005[4], "k:")
    data = bin2_HQ10000_G1_2_5_005[5][0]
    ax2.plot(data[:, 0], data[:, 1], "Brown", ls=":", lw=2, ms=7)
    data = bin2_HQ10000_G1_2_9_005[4][0]
    ax2.plot(data[:, 0], data[:, 1], "Orange", ls=":", lw=2, ms=7)
    Plt(2, bin2_HQ10000_G1_2_9_005[5], "y:")
    Plt(2, bin2_HQ10000_G1_0_10_009[4], "m:")
    Plt(2, bin2_HQ10000_G1_0_10_009[5], "c:")
    Plt(2, bin3_HQ10000_G1_0_0_000[4], "b-.")  # label=r'$\gamma = -2.5$'
    data, _ = bin3_HQ10000_G1_0_0_000[5]
    ax2.plot(data[:, 0], data[:, 1], "Skyblue", ls="-.", lw=2, ms=7)
    Plt(2, bin3_HQ10000_G1_2_1_005[4], "r-.")
    data, _ = bin3_HQ10000_G1_2_1_005[5]
    ax2.plot(data[:, 0], data[:, 1], "Pink", ls="-.", lw=2, ms=7)
    Plt(2, bin3_HQ10000_G0_8_2_005[4], "g-.")
    data, _ = bin3_HQ10000_G0_8_2_005[5]
    ax2.plot(data[:, 0], data[:, 1], "Chartreuse", ls="-.", lw=2, ms=7)
    Plt(2, bin3_HQ10000_G1_2_5_005[4], "k-.")
    data = bin3_HQ10000_G1_2_5_005[5][0]
    ax2.plot(data[:, 0], data[:, 1], "Brown", ls="-.", lw=2, ms=7)
    data = bin3_HQ10000_G1_2_9_005[4][0]
    ax2.plot(data[:, 0], data[:, 1], "Orange", ls="-.", lw=2, ms=7)
    Plt(2, bin3_HQ10000_G1_2_9_005[5], "y-.")
    Plt(2, bin3_HQ10000_G1_0_10_009[4], "m-.")
    Plt(2, bin3_HQ10000_G1_0_10_009[5], "c-.")
    Plt(2, bin4_HQ10000_G1_0_0_000[4], "b")  # label=r'$\gamma = -3.0$'
    data, _ = bin4_HQ10000_G1_0_0_000[5]
    ax2.plot(data[:, 0], data[:, 1], "Skyblue", lw=2, ms=7)
    Plt(2, bin4_HQ10000_G1_2_1_005[4], "r")
    data, _ = bin4_HQ10000_G1_2_1_005[5]
    ax2.plot(data[:, 0], data[:, 1], "Pink", lw=2, ms=7)
    Plt(2, bin4_HQ10000_G0_8_2_005[4], "g")
    data, _ = bin4_HQ10000_G0_8_2_005[5]
    ax2.plot(data[:, 0], data[:, 1], "Chartreuse", lw=2, ms=7)
    Plt(2, bin4_HQ10000_G1_2_5_005[4], "k")
    data, _ = bin4_HQ10000_G1_2_5_005[5]
    ax2.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
    data, _ = bin4_HQ10000_G1_2_9_005[4]
    ax2.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
    Plt(2, bin4_HQ10000_G1_2_9_005[5], "y")
    Plt(2, bin4_HQ10000_G1_0_10_009[4], "m")
    Plt(2, bin4_HQ10000_G1_0_10_009[5], "c")

    ax2.set_xlabel(
        r"$\log \left(|u_tn|,u_tp \right)$ and $\log \left(|u_rn|\
                   ,u_rp \right)$",
        fontsize=20,
    )
    ax2.set_ylabel(r"$f\left(\log \left( |u_n|,u_p \right)\right)$", fontsize=20)

    # label=r'$\gamma = -1.5$'
    Plt(3, bin1_HQ10000_G1_0_0_000[0], "b--", HQ0[9:])
    data, _ = bin1_HQ10000_G1_0_0_000[1]
    ax3.plot(data[:, 0], data[:, 1], "Skyblue", ls="--", lw=2, ms=7)
    Plt(3, bin1_HQ10000_G1_2_1_005[0], "r--", HQ12[9:])
    data, _ = bin1_HQ10000_G1_2_1_005[1]
    ax3.plot(data[:, 0], data[:, 1], "Pink", ls="--", lw=2, ms=7)
    Plt(3, bin1_HQ10000_G0_8_2_005[0], "g--", HQ18[9:])
    data, _ = bin1_HQ10000_G0_8_2_005[1]
    ax3.plot(data[:, 0], data[:, 1], "Chartreuse", ls="--", lw=2, ms=7)
    Plt(3, bin1_HQ10000_G1_2_5_005[0], "k--", HQ36[9:])
    data, _ = bin1_HQ10000_G1_2_5_005[1]
    ax3.plot(data[:, 0], data[:, 1], "Brown", ls="--", lw=2, ms=7)
    data, _ = bin1_HQ10000_G1_2_9_005[0]
    ax3.plot(data[:, 0], data[:, 1], "Orange", HQ60[9:], ls="--", lw=2, ms=7)
    Plt(3, bin1_HQ10000_G1_2_9_005[1], "y--")
    Plt(3, bin1_HQ10000_G1_0_10_009[0], HQ70[9:], "m--")
    Plt(3, bin1_HQ10000_G1_0_10_009[1], "c--")
    Plt(3, bin2_HQ10000_G1_0_0_000[0], "b:")  # label=r'$\gamma = -2.0$'
    data, _ = bin2_HQ10000_G1_0_0_000[1]
    ax3.plot(data[:, 0], data[:, 1], "Skyblue", ls=":", lw=4, ms=7)
    Plt(3, bin2_HQ10000_G1_2_1_005[0], "r:")
    data, _ = bin2_HQ10000_G1_2_1_005[1]
    ax3.plot(data[:, 0], data[:, 1], "Pink", ls=":", lw=4, ms=7)
    Plt(3, bin2_HQ10000_G0_8_2_005[0], "g:")
    data, _ = bin2_HQ10000_G0_8_2_005[1]
    ax3.plot(data[:, 0], data[:, 1], "Chartreuse", ls=":", lw=4, ms=7)
    Plt(3, bin2_HQ10000_G1_2_5_005[0], "k:")
    data, _ = bin2_HQ10000_G1_2_5_005[1]
    ax3.plot(data[:, 0], data[:, 1], "Brown", ls=":", lw=4, ms=7)
    data, _ = bin2_HQ10000_G1_2_9_005[0]
    ax3.plot(data[:, 0], data[:, 1], "Orange", ls=":", lw=4, ms=7)
    Plt(3, bin2_HQ10000_G1_2_9_005[1], "y:")
    Plt(3, bin2_HQ10000_G1_0_10_009[0], "m:")
    Plt(3, bin2_HQ10000_G1_0_10_009[1], "c:")
    Plt(3, bin3_HQ10000_G1_0_0_000[0], "b-.")  # label=r'$\gamma = -2.5$'
    data, _ = bin3_HQ10000_G1_0_0_000[1]
    ax3.plot(data[:, 0], data[:, 1], "Skyblue", ls="-.", lw=4, ms=7)
    Plt(3, bin3_HQ10000_G1_2_1_005[0], "r-.")
    data, _ = bin3_HQ10000_G1_2_1_005[1]
    ax3.plot(data[:, 0], data[:, 1], "Pink", ls="-.", lw=4, ms=7)
    Plt(3, bin3_HQ10000_G0_8_2_005[0], "g-.")
    data, _ = bin3_HQ10000_G0_8_2_005[1]
    ax3.plot(data[:, 0], data[:, 1], "Chartreuse", ls="-.", lw=4, ms=7)
    Plt(3, bin3_HQ10000_G1_2_5_005[0], "k-.")
    data, _ = bin3_HQ10000_G1_2_5_005[1]
    ax3.plot(data[:, 0], data[:, 1], "Brown", ls="-.", lw=4, ms=7)
    data, _ = bin3_HQ10000_G1_2_9_005[0]
    ax3.plot(data[:, 0], data[:, 1], "Orange", ls="-.", lw=4, ms=7)
    Plt(3, bin3_HQ10000_G1_2_9_005[1], "y-.")
    Plt(3, bin3_HQ10000_G1_0_10_009[0], "m-.")
    Plt(3, bin3_HQ10000_G1_0_10_009[1], "c-.")
    Plt(3, bin4_HQ10000_G1_0_0_000[0], "b")  # label=r'$\gamma = -3.0$'
    data, _ = bin4_HQ10000_G1_0_0_000[1]
    ax3.plot(data[:, 0], data[:, 1], "Skyblue", lw=2, ms=7)
    Plt(3, bin4_HQ10000_G1_2_1_005[0], "r")
    data, _ = bin4_HQ10000_G1_2_1_005[1]
    ax3.plot(data[:, 0], data[:, 1], "Pink", lw=2, ms=7)
    Plt(3, bin4_HQ10000_G0_8_2_005[0], "g")
    data, _ = bin4_HQ10000_G0_8_2_005[1]
    ax3.plot(data[:, 0], data[:, 1], "Chartreuse", lw=2, ms=7)
    Plt(3, bin4_HQ10000_G1_2_5_005[0], "k")
    data, _ = bin4_HQ10000_G1_2_5_005[1]
    ax3.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
    data, _ = bin4_HQ10000_G1_2_9_005[0]
    ax3.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
    Plt(3, bin4_HQ10000_G1_2_9_005[1], "y")
    Plt(3, bin4_HQ10000_G1_0_10_009[0], "m")
    Plt(3, bin4_HQ10000_G1_0_10_009[1], "c")

    ax3.set_xlabel(r"$u_t$ and $u_r$", fontsize=20)
    ax3.set_ylabel(r"$\log \left( f\left( u \right) \right)$", fontsize=20)
    ax3.set_yscale("log")

    # label=r'$\gamma = -1.5$'
    Plt(4, bin1_HQ10000_G1_0_0_000[4], "b--", HQ0[9:])
    data, _ = bin1_HQ10000_G1_0_0_000[5]
    ax4.plot(data[:, 0], data[:, 1], "Skyblue", ls="--", lw=2, ms=7)
    Plt(4, bin1_HQ10000_G1_2_1_005[4], "r--", HQ12[9:])
    data, _ = bin1_HQ10000_G1_2_1_005[5]
    ax4.plot(data[:, 0], data[:, 1], "Pink", ls="--", lw=2, ms=7)
    Plt(4, bin1_HQ10000_G0_8_2_005[4], "g--", HQ18[9:])
    data, _ = bin1_HQ10000_G0_8_2_005[5]
    ax4.plot(data[:, 0], data[:, 1], "Chartreuse", ls="--", lw=2, ms=7)
    Plt(4, bin1_HQ10000_G1_2_5_005[4], "k--", HQ36[9:])
    data, _ = bin1_HQ10000_G1_2_5_005[5]
    ax4.plot(data[:, 0], data[:, 1], "Brown", ls="--", lw=2, ms=7)
    data, _ = bin1_HQ10000_G1_2_9_005[4]
    ax4.plot(data[:, 0], data[:, 1], "Orange", HQ60[9:], ls="--", lw=2, ms=7)
    Plt(4, bin1_HQ10000_G1_2_9_005[5], "y--")
    Plt(4, bin1_HQ10000_G1_0_10_009[4], HQ70[9:], "m--")
    Plt(4, bin1_HQ10000_G1_0_10_009[5], "c--")
    Plt(4, bin2_HQ10000_G1_0_0_000[4], "b:")  # label=r'$\gamma = -2.0$'
    data, _ = bin2_HQ10000_G1_0_0_000[5]
    ax4.plot(data[:, 0], data[:, 1], "Skyblue", ls=":", lw=2, ms=7)
    Plt(4, bin2_HQ10000_G1_2_1_005[4], "r:")
    data, _ = bin2_HQ10000_G1_2_1_005[5]
    ax4.plot(data[:, 0], data[:, 1], "Pink", ls=":", lw=2, ms=7)
    Plt(4, bin2_HQ10000_G0_8_2_005[4], "g:")
    data, _ = bin2_HQ10000_G0_8_2_005[5]
    ax4.plot(data[:, 0], data[:, 1], "Chartreuse", ls=":", lw=2, ms=7)
    Plt(4, bin2_HQ10000_G1_2_5_005[4], "k:")
    data, _ = bin2_HQ10000_G1_2_5_005[5]
    ax4.plot(data[:, 0], data[:, 1], "Brown", ls=":", lw=2, ms=7)
    data, _ = bin2_HQ10000_G1_2_9_005[4]
    ax4.plot(data[:, 0], data[:, 1], "Orange", ls=":", lw=2, ms=7)
    Plt(4, bin2_HQ10000_G1_2_9_005[5], "y:")
    Plt(4, bin2_HQ10000_G1_0_10_009[4], "m:")
    Plt(4, bin2_HQ10000_G1_0_10_009[5], "c:")
    Plt(4, bin3_HQ10000_G1_0_0_000[4], "b-.")  # label=r'$\gamma = -2.5$'
    data, _ = bin3_HQ10000_G1_0_0_000[5]
    ax4.plot(data[:, 0], data[:, 1], "Skyblue", ls="-.", lw=2, ms=7)
    Plt(4, bin3_HQ10000_G1_2_1_005[4], "r-.")
    data, _ = bin3_HQ10000_G1_2_1_005[5]
    ax4.plot(data[:, 0], data[:, 1], "Pink", ls="-.", lw=2, ms=7)
    Plt(4, bin3_HQ10000_G0_8_2_005[4], "g-.")
    data, _ = bin3_HQ10000_G0_8_2_005[5]
    ax4.plot(data[:, 0], data[:, 1], "Chartreuse", ls="-.", lw=2, ms=7)
    Plt(4, bin3_HQ10000_G1_2_5_005[4], "k-.")
    data, _ = bin3_HQ10000_G1_2_5_005[5]
    ax4.plot(data[:, 0], data[:, 1], "Brown", ls="-.", lw=2, ms=7)
    data, _ = bin3_HQ10000_G1_2_9_005[4]
    ax4.plot(data[:, 0], data[:, 1], "Orange", ls="-.", lw=2, ms=7)
    Plt(4, bin3_HQ10000_G1_2_9_005[5], "y-.")
    Plt(4, bin3_HQ10000_G1_0_10_009[4], "m-.")
    Plt(4, bin3_HQ10000_G1_0_10_009[5], "c-.")
    Plt(4, bin4_HQ10000_G1_0_0_000[4], "b")  # label=r'$\gamma = -3.0$'
    data, _ = bin4_HQ10000_G1_0_0_000[5]
    ax4.plot(data[:, 0], data[:, 1], "Skyblue", lw=2, ms=7)
    Plt(4, bin4_HQ10000_G1_2_1_005[4], "r")
    data, _ = bin4_HQ10000_G1_2_1_005[5]
    ax4.plot(data[:, 0], data[:, 1], "Pink", lw=2, ms=7)
    Plt(4, bin4_HQ10000_G0_8_2_005[4], "g")
    data, _ = bin4_HQ10000_G0_8_2_005[5]
    ax4.plot(data[:, 0], data[:, 1], "Chartreuse", lw=2, ms=7)
    Plt(4, bin4_HQ10000_G1_2_5_005[4], "k")
    data, _ = bin4_HQ10000_G1_2_5_005[5]
    ax4.plot(data[:, 0], data[:, 1], "Brown", lw=2, ms=7)
    data, _ = bin4_HQ10000_G1_2_9_005[4]
    ax4.plot(data[:, 0], data[:, 1], "Orange", lw=2, ms=7)
    Plt(4, bin4_HQ10000_G1_2_9_005[5], "y")
    Plt(4, bin4_HQ10000_G1_0_10_009[4], "m")
    Plt(4, bin4_HQ10000_G1_0_10_009[5], "c")

    ax4.set_xlabel(
        r"$\log \left( |u_tn|,u_tp \right)$ and $\log \left(\
                   |u_rn|,u_rp \right)$",
        fontsize=20,
    )
    ax4.set_ylabel(
        r"$\log \left( f\left(\log \left( |u_n|,u_p \right)\right)\
                   \right)$",
        fontsize=20,
    )
    ax4.set_yscale("log")

if Fig3b_GPerts_G1_2_same_gammas_as_IC_vt:
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

    for i in range(1, 5):
        exec(f"ax{i}.grid()")

    for i in range(1, 5):
        exec(
            f"ax{i}.legend(prop=dict(size=13), numpoints=2, ncol=1,\
                            frameon=True, loc=0, handlelength=2.5)"
        )

    Plt(1, bin1_HQ10000_G1_2_1_005[0], "b--", HQ12[9:])
    Plt(1, bin1_HQ10000_G1_2_3_005[0], "r--", HQ24[9:])
    Plt(1, bin1_HQ10000_G1_2_5_005[0], "g--", HQ36[9:])
    Plt(1, bin1_HQ10000_G1_2_7_005[0], "k--", HQ48[9:])
    Plt(1, bin1_HQ10000_G1_2_9_005[0], "m--", HQ60[9:])
    Plt(1, bin2_HQ10000_G1_2_1_005[0], "r:")
    Plt(1, bin2_HQ10000_G1_2_3_005[0], "g:")
    Plt(1, bin2_HQ10000_G1_2_5_005[0], "k:")
    Plt(1, bin2_HQ10000_G1_2_7_005[0], "c:")
    Plt(1, bin2_HQ10000_G1_2_9_005[0], "m:")
    Plt(1, bin3_HQ10000_G1_2_1_005[0], "r-.")
    Plt(1, bin3_HQ10000_G1_2_3_005[0], "g-.")
    Plt(1, bin3_HQ10000_G1_2_5_005[0], "k-.")
    Plt(1, bin3_HQ10000_G1_2_7_005[0], "c-.")
    Plt(1, bin3_HQ10000_G1_2_9_005[0], "m-.")
    Plt(1, bin4_HQ10000_G1_2_1_005[0], "r")
    Plt(1, bin4_HQ10000_G1_2_3_005[0], "g")
    Plt(1, bin4_HQ10000_G1_2_5_005[0], "k")
    Plt(1, bin4_HQ10000_G1_2_7_005[0], "c")
    Plt(1, bin4_HQ10000_G1_2_9_005[0], "m")

    ax1.set_xlabel(r"$u_t$ and $u_r$", fontsize=20)
    ax1.set_ylabel(r"$f\left(u \right)$", fontsize=20)
    ax1.set_title(f"Time evolution of files: {HQ0[:-9]}", fontsize=20)

    Plt(2, bin1_HQ10000_G1_2_1_005[4], "r--", HQ12[9:])
    Plt(2, bin1_HQ10000_G1_2_3_005[4], "g--", HQ24[9:])
    Plt(2, bin1_HQ10000_G1_2_5_005[4], "k--", HQ36[9:])
    Plt(2, bin1_HQ10000_G1_2_7_005[4], "c--", HQ48[9:])
    Plt(2, bin1_HQ10000_G1_2_9_005[4], "m--", HQ60[9:])
    Plt(2, bin2_HQ10000_G1_2_1_005[4], "r:")
    Plt(2, bin2_HQ10000_G1_2_3_005[4], "g:")
    Plt(2, bin2_HQ10000_G1_2_5_005[4], "k:")
    Plt(2, bin2_HQ10000_G1_2_7_005[4], "c:")
    Plt(2, bin2_HQ10000_G1_2_9_005[4], "m:")
    Plt(2, bin3_HQ10000_G1_2_1_005[4], "r-.")
    Plt(2, bin3_HQ10000_G1_2_3_005[4], "g-.")
    Plt(2, bin3_HQ10000_G1_2_5_005[4], "k-.")
    Plt(2, bin3_HQ10000_G1_2_7_005[4], "c-.")
    Plt(2, bin3_HQ10000_G1_2_9_005[4], "m-.")
    Plt(2, bin4_HQ10000_G1_2_1_005[4], "r")
    Plt(2, bin4_HQ10000_G1_2_3_005[4], "g")
    Plt(2, bin4_HQ10000_G1_2_5_005[4], "k")
    Plt(2, bin4_HQ10000_G1_2_7_005[4], "c")
    Plt(2, bin4_HQ10000_G1_2_9_005[4], "m")

    ax2.set_xlabel(
        r"$\log \left( |u_tn|,u_tp \right)$ and $\log \left(\
                   |u_rn|,u_rp \right)$",
        fontsize=20,
    )
    ax2.set_ylabel(r"$f\left(\log \left( |u_n|,u_p \right)\right)$", fontsize=20)

    Plt(3, bin1_HQ10000_G1_2_1_005[0], "r--", HQ12[9:])
    Plt(3, bin1_HQ10000_G1_2_3_005[0], "g--", HQ24[9:])
    Plt(3, bin1_HQ10000_G1_2_5_005[0], "k--", HQ36[9:])
    Plt(3, bin1_HQ10000_G1_2_7_005[0], "c--", HQ48[9:])
    Plt(3, bin1_HQ10000_G1_2_9_005[0], "m--", HQ60[9:])
    Plt(3, bin2_HQ10000_G1_2_1_005[0], "r:")
    Plt(3, bin2_HQ10000_G1_2_3_005[0], "g:")
    Plt(3, bin2_HQ10000_G1_2_5_005[0], "k:")
    Plt(3, bin2_HQ10000_G1_2_7_005[0], "c:")
    Plt(3, bin2_HQ10000_G1_2_9_005[0], "m:")
    Plt(3, bin3_HQ10000_G1_2_1_005[0], "r-.")
    Plt(3, bin3_HQ10000_G1_2_3_005[0], "g-.")
    Plt(3, bin3_HQ10000_G1_2_5_005[0], "k-.")
    Plt(3, bin3_HQ10000_G1_2_7_005[0], "c-.")
    Plt(3, bin3_HQ10000_G1_2_9_005[0], "m-.")
    Plt(3, bin4_HQ10000_G1_2_1_005[0], "r")
    Plt(3, bin4_HQ10000_G1_2_3_005[0], "g")
    Plt(3, bin4_HQ10000_G1_2_5_005[0], "k")
    Plt(3, bin4_HQ10000_G1_2_7_005[0], "c")
    Plt(3, bin4_HQ10000_G1_2_9_005[0], "m")

    ax3.set_xlabel(r"$u_t$ and $u_r$", fontsize=20)
    ax3.set_ylabel(r"$\log \left( f\left( u \right) \right)$", fontsize=20)
    ax3.set_yscale("log")

    Plt(4, bin1_HQ10000_G1_2_1_005[4], "r--", HQ12[9:])
    Plt(4, bin1_HQ10000_G1_2_3_005[4], "g--", HQ24[9:])
    Plt(4, bin1_HQ10000_G1_2_5_005[4], "k--", HQ36[9:])
    Plt(4, bin1_HQ10000_G1_2_7_005[4], "c--", HQ48[9:])
    Plt(4, bin1_HQ10000_G1_2_9_005[4], "m--", HQ60[9:])
    Plt(4, bin2_HQ10000_G1_2_1_005[4], "r:")
    Plt(4, bin2_HQ10000_G1_2_3_005[4], "g:")
    Plt(4, bin2_HQ10000_G1_2_5_005[4], "k:")
    Plt(4, bin2_HQ10000_G1_2_7_005[4], "c:")
    Plt(4, bin2_HQ10000_G1_2_9_005[4], "m:")
    Plt(4, bin3_HQ10000_G1_2_1_005[4], "r-.")
    Plt(4, bin3_HQ10000_G1_2_3_005[4], "g-.")
    Plt(4, bin3_HQ10000_G1_2_5_005[4], "k-.")
    Plt(4, bin3_HQ10000_G1_2_7_005[4], "c-.")
    Plt(4, bin3_HQ10000_G1_2_9_005[4], "m-.")
    Plt(4, bin4_HQ10000_G1_2_1_005[4], "r")
    Plt(4, bin4_HQ10000_G1_2_3_005[4], "g")
    Plt(4, bin4_HQ10000_G1_2_5_005[4], "k")
    Plt(4, bin4_HQ10000_G1_2_7_005[4], "c")
    Plt(4, bin4_HQ10000_G1_2_9_005[4], "m")

    ax4.set_xlabel(
        r"$\log \left( |u_tn|,u_tp \right)$ and $\log \left(|u_rn|\
                   ,u_rp \right)$",
        fontsize=20,
    )
    ax4.set_ylabel(
        r"$\log \left( f\left(\log \left( |u_n|,u_p \right)\right)\
                   \right)$",
        fontsize=20,
    )
    ax4.set_yscale("log")

if Fig4_GPerts_different_gammas_vt:
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

    for i in range(1, 5):
        exec(f"ax{i}.grid()")

    ax1.set_xlabel(r"$u_t$", fontsize=20)
    ax1.set_ylabel(r"$f\left(u_t \right)$", fontsize=20)
    ax1.legend(
        prop=dict(size=18), numpoints=2, ncol=1, frameon=True, loc=0, handlelength=2.5
    )
    # ax2.set_xlim(-3, 0)
    ax2.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
    ax2.set_ylabel(r"$f\left(\log \left( |u_tn|,u_tp \right)\right)$", fontsize=20)
    ax3.set_xlabel(r"$u_t$", fontsize=20)
    ax3.set_ylabel(r"$\log \left( f\left( u_t \right) \right)$", fontsize=20)
    ax3.set_yscale("log")
    ax4.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
    ax4.set_ylabel(
        r"$\log\left(f\left(\log\left(|u_tn|,u_tp\right)\right)\
                   \right)$",
        fontsize=20,
    )
    ax4.set_yscale("log")

    if test:
        for i in range(2, 5):
            exec(
                f"ax{i}.legend(prop=dict(size=13), numpoints=2, ncol=1,\
                   frameon=True, loc=0, handlelength=2.5)"
            )

        Plt(1, bin1_different_gammas_HQ10000_G1_2_1_005[0], "b--", HQ12[9:])
        Plt(1, bin1_different_gammas_HQ10000_G1_2_3_005[0], "r--", HQ24[9:])
        Plt(1, bin1_different_gammas_HQ10000_G1_2_5_005[0], "g--", HQ36[9:])
        Plt(1, bin1_different_gammas_HQ10000_G1_2_7_005[0], "k--", HQ48[9:])
        Plt(1, bin1_different_gammas_HQ10000_G1_2_9_005[0], "m--", HQ60[9:])
        Plt(1, bin2_different_gammas_HQ10000_G1_2_1_005[0], "r:")
        Plt(1, bin2_different_gammas_HQ10000_G1_2_3_005[0], "g:")
        Plt(1, bin2_different_gammas_HQ10000_G1_2_5_005[0], "k:")
        Plt(1, bin2_different_gammas_HQ10000_G1_2_7_005[0], "c:")
        Plt(1, bin2_different_gammas_HQ10000_G1_2_9_005[0], "m:")
        Plt(1, bin3_different_gammas_HQ10000_G1_2_1_005[0], "r-.")
        Plt(1, bin3_different_gammas_HQ10000_G1_2_3_005[0], "g-.")
        Plt(1, bin3_different_gammas_HQ10000_G1_2_5_005[0], "k-.")
        Plt(1, bin3_different_gammas_HQ10000_G1_2_7_005[0], "c-.")
        Plt(1, bin3_different_gammas_HQ10000_G1_2_9_005[0], "m-.")
        Plt(1, bin4_different_gammas_HQ10000_G1_2_1_005[0], "r")
        Plt(1, bin4_different_gammas_HQ10000_G1_2_3_005[0], "g")
        Plt(1, bin4_different_gammas_HQ10000_G1_2_5_005[0], "k")
        Plt(1, bin4_different_gammas_HQ10000_G1_2_7_005[0], "c")
        Plt(1, bin4_different_gammas_HQ10000_G1_2_9_005[0], "m")
        ax1.set_title(
            "Time evolution of files=%s, different r bins" % HQ0[:-9], fontsize=20
        )

        Plt(2, bin1_different_gammas_HQ10000_G1_2_1_005[4], "r--", HQ12[9:])
        Plt(2, bin1_different_gammas_HQ10000_G1_2_3_005[4], "g--", HQ24[9:])
        Plt(2, bin1_different_gammas_HQ10000_G1_2_5_005[4], "k--", HQ36[9:])
        Plt(2, bin1_different_gammas_HQ10000_G1_2_7_005[4], "c--", HQ48[9:])
        Plt(2, bin1_different_gammas_HQ10000_G1_2_9_005[4], "m--", HQ60[9:])
        Plt(2, bin2_different_gammas_HQ10000_G1_2_1_005[4], "r:")
        Plt(2, bin2_different_gammas_HQ10000_G1_2_3_005[4], "g:")
        Plt(2, bin2_different_gammas_HQ10000_G1_2_5_005[4], "k:")
        Plt(2, bin2_different_gammas_HQ10000_G1_2_7_005[4], "c:")
        Plt(2, bin2_different_gammas_HQ10000_G1_2_9_005[4], "m:")
        Plt(2, bin3_different_gammas_HQ10000_G1_2_1_005[4], "r-.")
        Plt(2, bin3_different_gammas_HQ10000_G1_2_3_005[4], "g-.")
        Plt(2, bin3_different_gammas_HQ10000_G1_2_5_005[4], "k-.")
        Plt(2, bin3_different_gammas_HQ10000_G1_2_7_005[4], "c-.")
        Plt(2, bin3_different_gammas_HQ10000_G1_2_9_005[4], "m-.")
        Plt(2, bin4_different_gammas_HQ10000_G1_2_1_005[4], "r")
        Plt(2, bin4_different_gammas_HQ10000_G1_2_3_005[4], "g")
        Plt(2, bin4_different_gammas_HQ10000_G1_2_5_005[4], "k")
        Plt(2, bin4_different_gammas_HQ10000_G1_2_7_005[4], "c")
        Plt(2, bin4_different_gammas_HQ10000_G1_2_9_005[4], "m")

        Plt(3, bin1_different_gammas_HQ10000_G1_2_1_005[0], "r--", HQ12[9:])
        Plt(3, bin1_different_gammas_HQ10000_G1_2_3_005[0], "g--", HQ24[9:])
        Plt(3, bin1_different_gammas_HQ10000_G1_2_5_005[0], "k--", HQ36[9:])
        Plt(3, bin1_different_gammas_HQ10000_G1_2_7_005[0], "c--", HQ48[9:])
        Plt(3, bin1_different_gammas_HQ10000_G1_2_9_005[0], "m--", HQ60[9:])
        Plt(3, bin2_different_gammas_HQ10000_G1_2_1_005[0], "r:")
        Plt(3, bin2_different_gammas_HQ10000_G1_2_3_005[0], "g:")
        Plt(3, bin2_different_gammas_HQ10000_G1_2_5_005[0], "k:")
        Plt(3, bin2_different_gammas_HQ10000_G1_2_7_005[0], "c:")
        Plt(3, bin2_different_gammas_HQ10000_G1_2_9_005[0], "m:")
        Plt(3, bin3_different_gammas_HQ10000_G1_2_1_005[0], "r-.")
        Plt(3, bin3_different_gammas_HQ10000_G1_2_3_005[0], "g-.")
        Plt(3, bin3_different_gammas_HQ10000_G1_2_5_005[0], "k-.")
        Plt(3, bin3_different_gammas_HQ10000_G1_2_7_005[0], "c-.")
        Plt(3, bin3_different_gammas_HQ10000_G1_2_9_005[0], "m-.")
        Plt(3, bin4_different_gammas_HQ10000_G1_2_1_005[0], "r")
        Plt(3, bin4_different_gammas_HQ10000_G1_2_3_005[0], "g")
        Plt(3, bin4_different_gammas_HQ10000_G1_2_5_005[0], "k")
        Plt(3, bin4_different_gammas_HQ10000_G1_2_7_005[0], "c")
        Plt(3, bin4_different_gammas_HQ10000_G1_2_9_005[0], "m")

        Plt(4, bin1_different_gammas_HQ10000_G1_2_1_005[4], "r--", HQ12[9:])
        Plt(4, bin1_different_gammas_HQ10000_G1_2_3_005[4], "g--", HQ24[9:])
        Plt(4, bin1_different_gammas_HQ10000_G1_2_5_005[4], "k--", HQ36[9:])
        Plt(4, bin1_different_gammas_HQ10000_G1_2_7_005[4], "c--", HQ48[9:])
        Plt(4, bin1_different_gammas_HQ10000_G1_2_9_005[4], "m--", HQ60[9:])
        Plt(4, bin2_different_gammas_HQ10000_G1_2_1_005[4], "r:")
        Plt(4, bin2_different_gammas_HQ10000_G1_2_3_005[4], "g:")
        Plt(4, bin2_different_gammas_HQ10000_G1_2_5_005[4], "k:")
        Plt(4, bin2_different_gammas_HQ10000_G1_2_7_005[4], "c:")
        Plt(4, bin2_different_gammas_HQ10000_G1_2_9_005[4], "m:")
        Plt(4, bin3_different_gammas_HQ10000_G1_2_1_005[4], "r-.")
        Plt(4, bin3_different_gammas_HQ10000_G1_2_3_005[4], "g-.")
        Plt(4, bin3_different_gammas_HQ10000_G1_2_5_005[4], "k-.")
        Plt(4, bin3_different_gammas_HQ10000_G1_2_7_005[4], "c-.")
        Plt(4, bin3_different_gammas_HQ10000_G1_2_9_005[4], "m-.")
        Plt(4, bin4_different_gammas_HQ10000_G1_2_1_005[4], "r")
        Plt(4, bin4_different_gammas_HQ10000_G1_2_3_005[4], "g")
        Plt(4, bin4_different_gammas_HQ10000_G1_2_5_005[4], "k")
        Plt(4, bin4_different_gammas_HQ10000_G1_2_7_005[4], "c")
        Plt(4, bin4_different_gammas_HQ10000_G1_2_9_005[4], "m")

    if test2:
        Plt(1, bin1_different_gammas_test2_HQ10000_G1_0_0_000[0], "b--", test2_HQ0[15:])
        Plt(
            1, bin1_different_gammas_test2_HQ10000_G1_0_5_005[0], "r--", test2_HQ36[15:]
        )
        Plt(
            1,
            bin1_different_gammas_test2_HQ10000_G1_0_10_005[0],
            "g--",
            test2_HQ66[15:],
        )
        Plt(
            1,
            bin1_different_gammas_test2_HQ10000_G1_0_15_005[0],
            "k--",
            test2_HQ96[15:],
        )
        Plt(
            1,
            bin1_different_gammas_test2_HQ10000_G1_0_20_005[0],
            "m--",
            test2_HQ126[15:],
        )
        Plt(
            1,
            bin1_different_gammas_test2_HQ10000_G1_0_25_005[0],
            "b--",
            test2_HQ159[15:],
        )
        Plt(1, bin2_different_gammas_test2_HQ10000_G1_0_0_000[0], "r:")
        Plt(1, bin2_different_gammas_test2_HQ10000_G1_0_5_005[0], "g:")
        Plt(1, bin2_different_gammas_test2_HQ10000_G1_0_10_005[0], "k:")
        Plt(1, bin2_different_gammas_test2_HQ10000_G1_0_15_005[0], "c:")
        Plt(1, bin2_different_gammas_test2_HQ10000_G1_0_20_005[0], "m:")
        Plt(1, bin2_different_gammas_test2_HQ10000_G1_0_25_005[0], "b:")
        Plt(1, bin3_different_gammas_test2_HQ10000_G1_0_0_000[0], "r-.")
        Plt(1, bin3_different_gammas_test2_HQ10000_G1_0_5_005[0], "g-.")
        Plt(1, bin3_different_gammas_test2_HQ10000_G1_0_10_005[0], "k-.")
        Plt(1, bin3_different_gammas_test2_HQ10000_G1_0_15_005[0], "c-.")
        Plt(1, bin3_different_gammas_test2_HQ10000_G1_0_20_005[0], "m-.")
        Plt(1, bin3_different_gammas_test2_HQ10000_G1_0_25_005[0], "b-.")
        Plt(1, bin4_different_gammas_test2_HQ10000_G1_0_0_000[0], "r")
        Plt(1, bin4_different_gammas_test2_HQ10000_G1_0_5_005[0], "g")
        Plt(1, bin4_different_gammas_test2_HQ10000_G1_0_10_005[0], "k")
        Plt(1, bin4_different_gammas_test2_HQ10000_G1_0_15_005[0], "c")
        Plt(1, bin4_different_gammas_test2_HQ10000_G1_0_20_005[0], "m")
        Plt(1, bin4_different_gammas_test2_HQ10000_G1_0_25_005[0], "b")

        ax1.set_title(
            "Time evolution of files = %s, different r bins" % test2_HQ0[:-9],
            fontsize=20,
        )

        Plt(2, bin1_different_gammas_test2_HQ10000_G1_0_0_000[4], "b--")
        Plt(2, bin1_different_gammas_test2_HQ10000_G1_0_5_005[4], "r--")
        Plt(2, bin1_different_gammas_test2_HQ10000_G1_0_10_005[4], "g--")
        Plt(2, bin1_different_gammas_test2_HQ10000_G1_0_15_005[4], "k--")
        Plt(2, bin1_different_gammas_test2_HQ10000_G1_0_20_005[4], "m--")
        Plt(2, bin1_different_gammas_test2_HQ10000_G1_0_25_005[4], "b--")
        Plt(2, bin2_different_gammas_test2_HQ10000_G1_0_0_000[4], "r:")
        Plt(2, bin2_different_gammas_test2_HQ10000_G1_0_5_005[4], "g:")
        Plt(2, bin2_different_gammas_test2_HQ10000_G1_0_10_005[4], "k:")
        Plt(2, bin2_different_gammas_test2_HQ10000_G1_0_15_005[4], "c:")
        Plt(2, bin2_different_gammas_test2_HQ10000_G1_0_20_005[4], "m:")
        Plt(2, bin2_different_gammas_test2_HQ10000_G1_0_25_005[4], "b:")
        Plt(2, bin3_different_gammas_test2_HQ10000_G1_0_0_000[4], "r-.")
        Plt(2, bin3_different_gammas_test2_HQ10000_G1_0_5_005[4], "g-.")
        Plt(2, bin3_different_gammas_test2_HQ10000_G1_0_10_005[4], "k-.")
        Plt(2, bin3_different_gammas_test2_HQ10000_G1_0_15_005[4], "c-.")
        Plt(2, bin3_different_gammas_test2_HQ10000_G1_0_20_005[4], "m-.")
        Plt(2, bin3_different_gammas_test2_HQ10000_G1_0_25_005[4], "b-.")
        Plt(2, bin4_different_gammas_test2_HQ10000_G1_0_0_000[4], "r")
        Plt(2, bin4_different_gammas_test2_HQ10000_G1_0_5_005[4], "g")
        Plt(2, bin4_different_gammas_test2_HQ10000_G1_0_10_005[4], "k")
        Plt(2, bin4_different_gammas_test2_HQ10000_G1_0_15_005[4], "c")
        Plt(2, bin4_different_gammas_test2_HQ10000_G1_0_20_005[4], "m")
        Plt(2, bin4_different_gammas_test2_HQ10000_G1_0_25_005[4], "b")

        Plt(3, bin1_different_gammas_test2_HQ10000_G1_0_0_000[0], "b--")
        Plt(3, bin1_different_gammas_test2_HQ10000_G1_0_5_005[0], "r--")
        Plt(3, bin1_different_gammas_test2_HQ10000_G1_0_10_005[0], "g--")
        Plt(3, bin1_different_gammas_test2_HQ10000_G1_0_15_005[0], "k--")
        Plt(3, bin1_different_gammas_test2_HQ10000_G1_0_20_005[0], "m--")
        Plt(3, bin1_different_gammas_test2_HQ10000_G1_0_25_005[0], "b--")
        Plt(3, bin2_different_gammas_test2_HQ10000_G1_0_0_000[0], "r:")
        Plt(3, bin2_different_gammas_test2_HQ10000_G1_0_5_005[0], "g:")
        Plt(3, bin2_different_gammas_test2_HQ10000_G1_0_10_005[0], "k:")
        Plt(3, bin2_different_gammas_test2_HQ10000_G1_0_15_005[0], "c:")
        Plt(3, bin2_different_gammas_test2_HQ10000_G1_0_20_005[0], "m:")
        Plt(3, bin2_different_gammas_test2_HQ10000_G1_0_25_005[0], "b:")
        Plt(3, bin3_different_gammas_test2_HQ10000_G1_0_0_000[0], "r-.")
        Plt(3, bin3_different_gammas_test2_HQ10000_G1_0_5_005[0], "g-.")
        Plt(3, bin3_different_gammas_test2_HQ10000_G1_0_10_005[0], "k-.")
        Plt(3, bin3_different_gammas_test2_HQ10000_G1_0_15_005[0], "c-.")
        Plt(3, bin3_different_gammas_test2_HQ10000_G1_0_20_005[0], "m-.")
        Plt(3, bin3_different_gammas_test2_HQ10000_G1_0_25_005[0], "b-.")
        Plt(3, bin4_different_gammas_test2_HQ10000_G1_0_0_000[0], "r")
        Plt(3, bin4_different_gammas_test2_HQ10000_G1_0_5_005[0], "g")
        Plt(3, bin4_different_gammas_test2_HQ10000_G1_0_10_005[0], "k")
        Plt(3, bin4_different_gammas_test2_HQ10000_G1_0_15_005[0], "c")
        Plt(3, bin4_different_gammas_test2_HQ10000_G1_0_20_005[0], "m")
        Plt(3, bin4_different_gammas_test2_HQ10000_G1_0_25_005[0], "b")

        Plt(4, bin1_different_gammas_test2_HQ10000_G1_0_0_000[4], "b--")
        Plt(4, bin1_different_gammas_test2_HQ10000_G1_0_5_005[4], "r--")
        Plt(4, bin1_different_gammas_test2_HQ10000_G1_0_10_005[4], "g--")
        Plt(4, bin1_different_gammas_test2_HQ10000_G1_0_15_005[4], "k--")
        Plt(4, bin1_different_gammas_test2_HQ10000_G1_0_20_005[4], "m--")
        Plt(4, bin1_different_gammas_test2_HQ10000_G1_0_25_005[4], "b--")
        Plt(4, bin2_different_gammas_test2_HQ10000_G1_0_0_000[4], "r:")
        Plt(4, bin2_different_gammas_test2_HQ10000_G1_0_5_005[4], "g:")
        Plt(4, bin2_different_gammas_test2_HQ10000_G1_0_10_005[4], "k:")
        Plt(4, bin2_different_gammas_test2_HQ10000_G1_0_15_005[4], "c:")
        Plt(4, bin2_different_gammas_test2_HQ10000_G1_0_20_005[4], "m:")
        Plt(4, bin2_different_gammas_test2_HQ10000_G1_0_25_005[4], "b:")
        Plt(4, bin3_different_gammas_test2_HQ10000_G1_0_0_000[4], "r-.")
        Plt(4, bin3_different_gammas_test2_HQ10000_G1_0_5_005[4], "g-.")
        Plt(4, bin3_different_gammas_test2_HQ10000_G1_0_10_005[4], "k-.")
        Plt(4, bin3_different_gammas_test2_HQ10000_G1_0_15_005[4], "c-.")
        Plt(4, bin3_different_gammas_test2_HQ10000_G1_0_20_005[4], "m-.")
        Plt(4, bin3_different_gammas_test2_HQ10000_G1_0_25_005[4], "b-.")
        Plt(4, bin4_different_gammas_test2_HQ10000_G1_0_0_000[4], "r")
        Plt(4, bin4_different_gammas_test2_HQ10000_G1_0_5_005[4], "g")
        Plt(4, bin4_different_gammas_test2_HQ10000_G1_0_10_005[4], "k")
        Plt(4, bin4_different_gammas_test2_HQ10000_G1_0_15_005[4], "c")
        Plt(4, bin4_different_gammas_test2_HQ10000_G1_0_20_005[4], "m")
        Plt(4, bin4_different_gammas_test2_HQ10000_G1_0_25_005[4], "b")

    if B:
        Plt(1, bin1_different_gammas_B_HQ10000_G1_0_0_000[0], "r--", B_HQ0[11:])
        Plt(1, bin1_different_gammas_B_HQ10000_G1_0_5_005[0], "g--", B_HQ36[11:])
        Plt(1, bin1_different_gammas_B_HQ10000_G1_0_10_005[0], "k--", B_HQ66[11:])
        Plt(1, bin1_different_gammas_B_HQ10000_G1_0_198_000[0], "c--", B_HQ294[11:])
        Plt(1, bin1_different_gammas_B_HQ10000_G1_0_198_093[0], "m--", B_HQ382[11:])
        Plt(1, bin2_different_gammas_B_HQ10000_G1_0_0_000[0], "r:")
        Plt(1, bin2_different_gammas_B_HQ10000_G1_0_5_005[0], "g:")
        Plt(1, bin2_different_gammas_B_HQ10000_G1_0_10_005[0], "k:")
        Plt(1, bin2_different_gammas_B_HQ10000_G1_0_198_000[0], "c:")
        Plt(1, bin2_different_gammas_B_HQ10000_G1_0_198_093[0], "m:")
        Plt(1, bin3_different_gammas_B_HQ10000_G1_0_0_000[0], "r-.")
        Plt(1, bin3_different_gammas_B_HQ10000_G1_0_5_005[0], "g-.")
        Plt(1, bin3_different_gammas_B_HQ10000_G1_0_10_005[0], "k-.")
        Plt(1, bin3_different_gammas_B_HQ10000_G1_0_198_000[0], "c-.")
        Plt(1, bin3_different_gammas_B_HQ10000_G1_0_198_093[0], "m-.")
        Plt(1, bin4_different_gammas_B_HQ10000_G1_0_0_000[0], "r")
        Plt(1, bin4_different_gammas_B_HQ10000_G1_0_5_005[0], "g")
        Plt(1, bin4_different_gammas_B_HQ10000_G1_0_10_005[0], "k")
        Plt(1, bin4_different_gammas_B_HQ10000_G1_0_198_000[0], "c")
        Plt(1, bin4_different_gammas_B_HQ10000_G1_0_198_093[0], "m")
        ax1.set_title(
            "Time evolution of files = %s, different r bins" % B_HQ0[:-9], fontsize=20
        )

        Plt(2, bin1_different_gammas_B_HQ10000_G1_0_0_000[4], "r--")
        Plt(2, bin1_different_gammas_B_HQ10000_G1_0_5_005[4], "g--")
        Plt(2, bin1_different_gammas_B_HQ10000_G1_0_10_005[4], "k--")
        Plt(2, bin1_different_gammas_B_HQ10000_G1_0_198_000[4], "c--")
        Plt(2, bin1_different_gammas_B_HQ10000_G1_0_198_093[4], "m--")
        Plt(2, bin2_different_gammas_B_HQ10000_G1_0_0_000[4], "r:")
        Plt(2, bin2_different_gammas_B_HQ10000_G1_0_5_005[4], "g:")
        Plt(2, bin2_different_gammas_B_HQ10000_G1_0_10_005[4], "k:")
        Plt(2, bin2_different_gammas_B_HQ10000_G1_0_198_000[4], "c:")
        Plt(2, bin2_different_gammas_B_HQ10000_G1_0_198_093[4], "m:")
        Plt(2, bin3_different_gammas_B_HQ10000_G1_0_0_000[4], "r-.")
        Plt(2, bin3_different_gammas_B_HQ10000_G1_0_5_005[4], "g-.")
        Plt(2, bin3_different_gammas_B_HQ10000_G1_0_10_005[4], "k-.")
        Plt(2, bin3_different_gammas_B_HQ10000_G1_0_198_000[4], "c-.")
        Plt(2, bin3_different_gammas_B_HQ10000_G1_0_198_093[4], "m-.")
        Plt(2, bin4_different_gammas_B_HQ10000_G1_0_0_000[4], "r")
        Plt(2, bin4_different_gammas_B_HQ10000_G1_0_5_005[4], "g")
        Plt(2, bin4_different_gammas_B_HQ10000_G1_0_10_005[4], "k")
        Plt(2, bin4_different_gammas_B_HQ10000_G1_0_198_000[4], "c")
        Plt(2, bin4_different_gammas_B_HQ10000_G1_0_198_093[4], "m")

        Plt(3, bin1_different_gammas_B_HQ10000_G1_0_0_000[0], "r--")
        Plt(3, bin1_different_gammas_B_HQ10000_G1_0_5_005[0], "g--")
        Plt(3, bin1_different_gammas_B_HQ10000_G1_0_10_005[0], "k--")
        Plt(3, bin1_different_gammas_B_HQ10000_G1_0_198_000[0], "c--")
        Plt(3, bin1_different_gammas_B_HQ10000_G1_0_198_093[0], "m--")
        Plt(3, bin2_different_gammas_B_HQ10000_G1_0_0_000[0], "r:")
        Plt(3, bin2_different_gammas_B_HQ10000_G1_0_5_005[0], "g:")
        Plt(3, bin2_different_gammas_B_HQ10000_G1_0_10_005[0], "k:")
        Plt(3, bin2_different_gammas_B_HQ10000_G1_0_198_000[0], "c:")
        Plt(3, bin2_different_gammas_B_HQ10000_G1_0_198_093[0], "m:")
        Plt(3, bin3_different_gammas_B_HQ10000_G1_0_0_000[0], "r-.")
        Plt(3, bin3_different_gammas_B_HQ10000_G1_0_5_005[0], "g-.")
        Plt(3, bin3_different_gammas_B_HQ10000_G1_0_10_005[0], "k-.")
        Plt(3, bin3_different_gammas_B_HQ10000_G1_0_198_000[0], "c-.")
        Plt(3, bin3_different_gammas_B_HQ10000_G1_0_198_093[0], "m-.")
        Plt(3, bin4_different_gammas_B_HQ10000_G1_0_0_000[0], "r")
        Plt(3, bin4_different_gammas_B_HQ10000_G1_0_5_005[0], "g")
        Plt(3, bin4_different_gammas_B_HQ10000_G1_0_10_005[0], "k")
        Plt(3, bin4_different_gammas_B_HQ10000_G1_0_198_000[0], "c")
        Plt(3, bin4_different_gammas_B_HQ10000_G1_0_198_093[0], "m")

        Plt(4, bin1_different_gammas_B_HQ10000_G1_0_0_000[4], "r--")
        Plt(4, bin1_different_gammas_B_HQ10000_G1_0_5_005[4], "g--")
        Plt(4, bin1_different_gammas_B_HQ10000_G1_0_10_005[4], "k--")
        Plt(4, bin1_different_gammas_B_HQ10000_G1_0_198_000[4], "c--")
        Plt(4, bin1_different_gammas_B_HQ10000_G1_0_198_093[4], "m--")
        Plt(4, bin2_different_gammas_B_HQ10000_G1_0_0_000[4], "r:")
        Plt(4, bin2_different_gammas_B_HQ10000_G1_0_5_005[4], "g:")
        Plt(4, bin2_different_gammas_B_HQ10000_G1_0_10_005[4], "k:")
        Plt(4, bin2_different_gammas_B_HQ10000_G1_0_198_000[4], "c:")
        Plt(4, bin2_different_gammas_B_HQ10000_G1_0_198_093[4], "m:")
        Plt(4, bin3_different_gammas_B_HQ10000_G1_0_0_000[4], "r-.")
        Plt(4, bin3_different_gammas_B_HQ10000_G1_0_5_005[4], "g-.")
        Plt(4, bin3_different_gammas_B_HQ10000_G1_0_10_005[4], "k-.")
        Plt(4, bin3_different_gammas_B_HQ10000_G1_0_198_000[4], "c-.")
        Plt(4, bin3_different_gammas_B_HQ10000_G1_0_198_093[4], "m-.")
        Plt(4, bin4_different_gammas_B_HQ10000_G1_0_0_000[4], "r")
        Plt(4, bin4_different_gammas_B_HQ10000_G1_0_5_005[4], "g")
        Plt(4, bin4_different_gammas_B_HQ10000_G1_0_10_005[4], "k")
        Plt(4, bin4_different_gammas_B_HQ10000_G1_0_198_000[4], "c")
        Plt(4, bin4_different_gammas_B_HQ10000_G1_0_198_093[4], "m")

if Fig5a_GPerts_gammas_1_5_vt_divided_by_gauss_and_Tsallis:
    f, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(4, 2)

    ax1.set_ylabel(r"$f\left(u \right)$", fontsize=20)
    ax2.set_ylabel(r"$f\left(\log \left( |u_n|,u_p \right)\right)$", fontsize=20)
    ax3.set_ylabel(r"$\log \left( f\left( u \right) \right)$", fontsize=20)
    ax3.set_yscale("log")
    ax4.set_ylabel(
        r"$\log \left( f\left(\log \left(|u_n|,u_p\right)\
                   \right)\right)$",
        fontsize=20,
    )
    ax4.set_yscale("log")

    if test:
        for i in range(1, 7):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(
                f"ax{i}.legend(prop=dict(size=13), numpoints=2, ncol=1,\
                   frameon=True, loc=0, handlelength=2.5)"
            )

        for i in range(1, 7):
            exec(f"ax{i}.set_xticklabels([])")

        Plt(1, bin1_different_gammas_HQ10000_G1_2_1_005[0], "b")
        Plt(1, bin1_different_gammas_HQ10000_G1_2_3_005[0], "r")
        Plt(1, bin1_different_gammas_HQ10000_G1_2_5_005[0], "g")
        Plt(1, bin1_different_gammas_HQ10000_G1_2_7_005[0], "k")
        Plt(1, bin1_different_gammas_HQ10000_G1_2_9_005[0], "c")
        ax1.set_title(
            r"Time evolution of files = %s, different r bins,\
                      $\gamma = -1.5$"
            % HQ0[:-9],
            fontsize=20,
        )

        Plt(2, bin1_different_gammas_HQ10000_G1_2_1_005[4], "r", HQ12[9:])
        Plt(2, bin1_different_gammas_HQ10000_G1_2_3_005[4], "g", HQ24[9:])
        Plt(2, bin1_different_gammas_HQ10000_G1_2_5_005[4], "k", HQ36[9:])
        Plt(2, bin1_different_gammas_HQ10000_G1_2_7_005[4], "c", HQ48[9:])
        Plt(2, bin1_different_gammas_HQ10000_G1_2_9_005[4], "m", HQ60[9:])

        Plt(3, bin1_different_gammas_HQ10000_G1_2_1_005[0], "r")
        Plt(3, bin1_different_gammas_HQ10000_G1_2_3_005[0], "g")
        Plt(3, bin1_different_gammas_HQ10000_G1_2_5_005[0], "k")
        Plt(3, bin1_different_gammas_HQ10000_G1_2_7_005[0], "c")
        Plt(3, bin1_different_gammas_HQ10000_G1_2_9_005[0], "m")

        Plt(4, bin1_different_gammas_HQ10000_G1_2_1_005[4], "r")
        Plt(4, bin1_different_gammas_HQ10000_G1_2_3_005[4], "g")
        Plt(4, bin1_different_gammas_HQ10000_G1_2_5_005[4], "k")
        Plt(4, bin1_different_gammas_HQ10000_G1_2_7_005[4], "c")
        Plt(4, bin1_different_gammas_HQ10000_G1_2_9_005[4], "m")

        def denom_ax5(a):
            return np.log10(a) * np.exp(-0.5 * a**2)

        d, _ = bin1_different_gammas_HQ10000_G1_2_1_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin1_different_gammas_HQ10000_G1_2_3_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin1_different_gammas_HQ10000_G1_2_5_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "k", lw=2, ms=7)
        d = bin1_different_gammas_HQ10000_G1_2_7_005[0][0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "c", lw=2, ms=7)
        d = bin1_different_gammas_HQ10000_G1_2_9_005[0][0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "m", lw=2, ms=7)
        ax5.set_ylabel(r"$\frac{f\left( u \right)}{log(x)e^{-0.5x^2}}$", fontsize=20)

        def denom_ax6(a):
            return np.exp(-0.5 * a**2)

        d, _ = bin1_different_gammas_HQ10000_G1_2_1_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin1_different_gammas_HQ10000_G1_2_3_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin1_different_gammas_HQ10000_G1_2_5_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "k", lw=2, ms=7)
        d = bin1_different_gammas_HQ10000_G1_2_7_005[4][0]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "c", lw=2, ms=7)
        d = bin1_different_gammas_HQ10000_G1_2_9_005[4][0]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "m", lw=2, ms=7)
        ax6.set_ylabel(
            r"$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}\
                       {e^{-0.5x^2}}$",
            fontsize=20,
        )

    else:
        ax7.set_xlabel(r"$u_t$", fontsize=20)
        ax7.set_ylabel(r"$\frac{f\left(u \right)}{Tsallis}$", fontsize=20)
        ax8.set_xlabel(r"$\log \left(|u_tn|,u_tp \right)$", fontsize=20)
        ax8.set_ylabel(
            r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}\
                       {Tsallis}$",
            fontsize=20,
        )

    if test2:
        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        for i in range(1, 3):
            exec(
                f"ax{i}.legend(prop=dict(size=13), numpoints=2, ncol=1,\
                 frameon=True, loc=0, handlelength=2.5)"
            )

        for i in range(1, 7):
            exec(f"ax{i}.set_xticklabels([])")

        Plt(1, bin1_different_gammas_test2_HQ10000_G1_0_0_000[0], "r")
        Plt(1, bin1_different_gammas_test2_HQ10000_G1_0_5_005[0], "g")
        Plt(1, bin1_different_gammas_test2_HQ10000_G1_0_10_005[0], "k")
        Plt(1, bin1_different_gammas_test2_HQ10000_G1_0_15_005[0], "c")
        Plt(1, bin1_different_gammas_test2_HQ10000_G1_0_20_005[0], "m")
        Plt(1, bin1_different_gammas_test2_HQ10000_G1_0_25_005[0], "b")
        ax1.set_title(
            r"Time evolution of files = %s, different r bins,\
                      $\gamma = -1.5$"
            % test2_HQ0[:-9],
            fontsize=20,
        )

        Plt(2, bin1_different_gammas_test2_HQ10000_G1_0_0_000[4], "r", test2_HQ0[15:])
        Plt(2, bin1_different_gammas_test2_HQ10000_G1_0_5_005[4], "g", test2_HQ36[15:])
        Plt(2, bin1_different_gammas_test2_HQ10000_G1_0_10_005[4], "k", test2_HQ66[15:])
        Plt(2, bin1_different_gammas_test2_HQ10000_G1_0_15_005[4], "c", test2_HQ96[15:])
        Plt(
            2, bin1_different_gammas_test2_HQ10000_G1_0_20_005[4], "m", test2_HQ126[15:]
        )
        Plt(
            2, bin1_different_gammas_test2_HQ10000_G1_0_25_005[4], "b", test2_HQ159[15:]
        )

        Plt(3, bin1_different_gammas_test2_HQ10000_G1_0_0_000[0], "r")
        Plt(3, bin1_different_gammas_test2_HQ10000_G1_0_5_005[0], "g")
        Plt(3, bin1_different_gammas_test2_HQ10000_G1_0_10_005[0], "k")
        Plt(3, bin1_different_gammas_test2_HQ10000_G1_0_15_005[0], "c")
        Plt(3, bin1_different_gammas_test2_HQ10000_G1_0_20_005[0], "m")
        Plt(3, bin1_different_gammas_test2_HQ10000_G1_0_25_005[0], "b")

        Plt(4, bin1_different_gammas_test2_HQ10000_G1_0_0_000[4], "r")
        Plt(4, bin1_different_gammas_test2_HQ10000_G1_0_5_005[4], "g")
        Plt(4, bin1_different_gammas_test2_HQ10000_G1_0_10_005[4], "k")
        Plt(4, bin1_different_gammas_test2_HQ10000_G1_0_15_005[4], "c")
        Plt(4, bin1_different_gammas_test2_HQ10000_G1_0_20_005[4], "m")
        Plt(4, bin1_different_gammas_test2_HQ10000_G1_0_25_005[4], "b")

        def denom_ax5(a):
            return 887.569 * a * np.exp(-0.922 * a**2)

        d, _ = bin1_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin1_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin1_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin1_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "c", lw=2, ms=7)
        d, _ = bin1_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "m", lw=2, ms=7)
        d, _ = bin1_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "b", lw=2, ms=7)
        ax5.set_ylabel(
            r"$\frac{f\left( u \right)}{887.569 \cdot x \cdot\
                         e^{-0.922 \cdot x^2} }$",
            fontsize=20,
        )

        def denom_ax6(a):
            return 3424.993 * (10**a) ** 2 * np.exp(-0.930 * (10**a) ** 2)

        d, _ = bin1_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin1_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin1_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin1_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "c", lw=2, ms=7)
        d, _ = bin1_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "m", lw=2, ms=7)
        d, _ = bin1_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "b", lw=2, ms=7)
        ax6.set_ylim(0, 5)
        ax6.set_ylabel(
            r"$\frac{f\left(\log \left(|u_tn|,u_tp \right)\right)}\
                       {3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2}}$",
            fontsize=20,
        )

        def denom_ax7(a):
            return (
                864.543
                * a
                * (1 - (1 - 0.946) * 0.908 * a**2) ** (0.946 / (1 - 0.946))
            )

        d, _ = bin1_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin1_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin1_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin1_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "c", lw=2, ms=7)
        d, _ = bin1_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "m", lw=2, ms=7)
        d, _ = bin1_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "b", lw=2, ms=7)
        ax7.set_ylim(0, 2)

        def denom_ax8(a):
            return (
                3391.113
                * 10**a
                * (1 - (1 - 0.987) * 0.924 * 10 ** (a**2)) ** (0.987 / (1.0 - 0.987))
            )

        d, _ = bin1_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin1_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin1_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin1_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "c", lw=2, ms=7)
        d, _ = bin1_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "m", lw=2, ms=7)
        d, _ = bin1_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "b", lw=2, ms=7)
        ax8.set_ylim(0, 5)

    if A:
        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.set_xticklabels([])")

        for i in range(1, 7):
            exec(
                f"legend(prop=dict(size=13), numpoints=2, ncol=1,\
                          frameon=True, loc=0, handlelength=2.5)"
            )

        Plt(1, bin1_different_gammas_A_HQ10000_G1_0_0_000[0], "r")
        Plt(1, bin1_different_gammas_A_HQ10000_G1_0_5_005[0], "g")
        Plt(1, bin1_different_gammas_A_HQ10000_G1_0_10_005[0], "k")
        Plt(1, bin1_different_gammas_A_HQ10000_G1_0_40_005[0], "c")
        Plt(1, bin1_different_gammas_A_HQ10000_G1_0_48_009[0], "m")
        Plt(1, bin1_different_gammas_A_HQ10000_G1_0_48_093[0], "b")
        ax1.set_title(
            r"Time evolution of %s, different r bins,\
                      $\gamma = -1.5$"
            % A_HQ0[:-9],
            fontsize=20,
        )

        Plt(2, bin1_different_gammas_A_HQ10000_G1_0_0_000[4], "r", A_HQ0[11:])
        Plt(2, bin1_different_gammas_A_HQ10000_G1_0_5_005[4], "g", A_HQ36[11:])
        Plt(2, bin1_different_gammas_A_HQ10000_G1_0_10_005[4], "k", A_HQ66[11:])
        Plt(2, bin1_different_gammas_A_HQ10000_G1_0_40_005[4], "c", A_HQ246[11:])
        Plt(2, bin1_different_gammas_A_HQ10000_G1_0_48_009[4], "m", A_HQ298[11:])
        Plt(2, bin1_different_gammas_A_HQ10000_G1_0_48_093[4], "b", A_HQ382[11:])

        Plt(3, bin1_different_gammas_A_HQ10000_G1_0_0_000[0], "r")
        Plt(3, bin1_different_gammas_A_HQ10000_G1_0_5_005[0], "g")
        Plt(3, bin1_different_gammas_A_HQ10000_G1_0_10_005[0], "k")
        Plt(3, bin1_different_gammas_A_HQ10000_G1_0_40_005[0], "c")
        Plt(3, bin1_different_gammas_A_HQ10000_G1_0_48_009[0], "m")
        Plt(3, bin1_different_gammas_A_HQ10000_G1_0_48_093[0], "b")

        Plt(4, bin1_different_gammas_A_HQ10000_G1_0_0_000[4], "r")
        Plt(4, bin1_different_gammas_A_HQ10000_G1_0_5_005[4], "g")
        Plt(4, bin1_different_gammas_A_HQ10000_G1_0_10_005[4], "k")
        Plt(4, bin1_different_gammas_A_HQ10000_G1_0_40_005[4], "c")
        Plt(4, bin1_different_gammas_A_HQ10000_G1_0_48_009[4], "m")
        Plt(4, bin1_different_gammas_A_HQ10000_G1_0_48_093[4], "b")

        def denom_ax5(a):
            return 887.569 * a * np.exp(-0.922 * a**2)

        d, _ = bin1_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin1_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin1_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin1_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "c", lw=2, ms=7)
        d, _ = bin1_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "m", lw=2, ms=7)
        d, _ = bin1_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "b", lw=2, ms=7)
        ax5.set_ylim(0.5, 1.5)
        ax5.set_ylabel(
            r"$\frac{f\left( u \right)}{887.569 \cdot x \cdot\
                       e^{-0.922 \cdot x^2}}$",
            fontsize=20,
        )

        def denom_ax6(a):
            return 3424.993 * (10**a) ** 2 * np.exp(-0.930 * (10**a) ** 2)

        d, _ = bin1_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin1_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin1_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin1_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "c", lw=2, ms=7)
        d, _ = bin1_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "m", lw=2, ms=7)
        d, _ = bin1_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "b", lw=2, ms=7)
        ax6.set_ylim(0.5, 1.5)
        ax6.set_ylabel(
            r"$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}\
                       {3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$",
            fontsize=20,
        )

        def denom_ax7(a):
            return (
                864.543
                * a
                * (1 - (1 - 0.946) * 0.908 * a**2) ** (0.946 / (1 - 0.946))
            )

        d, _ = bin1_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin1_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin1_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin1_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "c", lw=2, ms=7)
        d, _ = bin1_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "m", lw=2, ms=7)
        d, _ = bin1_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "b", lw=2, ms=7)
        ax7.set_ylim(0.5, 1.5)

        def denom_ax8(a):
            return (
                3391.113
                * 10**a
                * (1 - (1 - 0.987) * 0.924 * 10 ** (a**2)) ** (0.987 / (1.0 - 0.987))
            )

        d, _ = bin1_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin1_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin1_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin1_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "c", lw=2, ms=7)
        d, _ = bin1_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "m", lw=2, ms=7)
        d, _ = bin1_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "b", lw=2, ms=7)
        ax8.set_ylim(0.5, 1.5)

    if B:
        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.set_xticklabels([])")

        for i in range(1, 7):
            exec(
                f"legend(prop=dict(size=13), numpoints=2, ncol=1,\
                          frameon=True, loc=0, handlelength=2.5)"
            )

        Plt(1, bin1_different_gammas_B_HQ10000_G1_0_0_000[0], "r")
        Plt(1, bin1_different_gammas_B_HQ10000_G1_0_5_005[0], "g")
        Plt(1, bin1_different_gammas_B_HQ10000_G1_0_10_005[0], "k")
        Plt(1, bin1_different_gammas_B_HQ10000_G1_0_198_000[0], "c")
        Plt(1, bin1_different_gammas_B_HQ10000_G1_0_198_093[0], "m")
        ax1.set_title(
            r"Time evolution of %s, different r bins,\
                      $\gamma = -1.5$"
            % B_HQ0[:-9],
            fontsize=20,
        )

        Plt(2, bin1_different_gammas_B_HQ10000_G1_0_0_000[4], "r", B_HQ0[11:])
        Plt(2, bin1_different_gammas_B_HQ10000_G1_0_5_005[4], "g", B_HQ36[11:])
        Plt(2, bin1_different_gammas_B_HQ10000_G1_0_10_005[4], "k", B_HQ66[11:])
        Plt(2, bin1_different_gammas_B_HQ10000_G1_0_198_000[4], "c", B_HQ294[11:])
        Plt(2, bin1_different_gammas_B_HQ10000_G1_0_198_093[4], "m", B_HQ382[11:])

        Plt(3, bin1_different_gammas_B_HQ10000_G1_0_0_000[0], "r")
        Plt(3, bin1_different_gammas_B_HQ10000_G1_0_5_005[0], "g")
        Plt(3, bin1_different_gammas_B_HQ10000_G1_0_10_005[0], "k")
        Plt(3, bin1_different_gammas_B_HQ10000_G1_0_198_000[0], "c")
        Plt(3, bin1_different_gammas_B_HQ10000_G1_0_198_093[0], "m")

        Plt(4, bin1_different_gammas_B_HQ10000_G1_0_0_000[4], "r")
        Plt(4, bin1_different_gammas_B_HQ10000_G1_0_5_005[4], "g")
        Plt(4, bin1_different_gammas_B_HQ10000_G1_0_10_005[4], "k")
        Plt(4, bin1_different_gammas_B_HQ10000_G1_0_198_000[4], "c")
        Plt(4, bin1_different_gammas_B_HQ10000_G1_0_198_093[4], "m")

        def denom_ax5(a):
            return 914.415 * a * np.exp(-0.930 * a**2)

        d, _ = bin1_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin1_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin1_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin1_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "c", lw=2, ms=7)
        d, _ = bin1_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "m", lw=2, ms=7)
        ax5.set_ylabel(
            r"$\frac{f\left( u \right)}{914.415 \cdot x \cdot\
                       e^{-0.930 \cdot x^2}}$",
            fontsize=20,
        )

        def denom_ax6(a):
            return 3452.955 * (10**a) ** 2 * np.exp(-0.936 * (10**a) ** 2)

        d, _ = bin1_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin1_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin1_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin1_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "c", lw=2, ms=7)
        d, _ = bin1_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "m", lw=2, ms=7)
        ax6.set_ylim(0, 3)
        ax6.set_ylabel(
            r"$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}\
                       {3452.955 \cdot x^2 \cdot e^{-0.936 \cdot x^2}}$",
            fontsize=20,
        )

        def denom_ax7(a):
            return (
                894.292
                * a
                * (1 - (1 - 0.955) * 0.918 * a**2) ** (0.955 / (1 - 0.955))
            )

        d, _ = bin1_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin1_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin1_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin1_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "c", lw=2, ms=7)
        d, _ = bin1_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "m", lw=2, ms=7)
        ax7.set_ylim(0, 2)

        def denom_ax8(a):
            return (
                3418.569
                * 10**a
                * (1 - (1 - 0.987) * 0.929 * 10 ** (a**2)) ** (0.987 / (1.0 - 0.987))
            )

        d, _ = bin1_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin1_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin1_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin1_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "c", lw=2, ms=7)
        d, _ = bin1_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "m", lw=2, ms=7)
        ax8.set_ylim(0, 5)

if Fig5b_GPerts_gammas_2_0_vt_divided_by_gauss_and_Tsallis:
    f, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(4, 2)

    ax1.set_ylabel(r"$f\left( u \right)$", fontsize=20)
    ax2.set_ylabel(r"$f\left(\log \left(|u_n|,u_p \right)\right)$", fontsize=20)
    ax3.set_ylabel(r"$\log \left( f\left( u \right) \right)$", fontsize=20)
    ax3.set_yscale("log")
    ax4.set_ylabel(
        r"$\log \left( f\left(\log \left( |u_n|,u_p \right)\
                   \right) \right)$",
        fontsize=20,
    )
    ax4.set_yscale("log")

    if test:
        for i in range(1, 7):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.set_xticklabels([])")

        for i in range(1, 7):
            exec(
                f"legend(prop=dict(size=13), numpoints=2, ncol=1,\
                          frameon=True, loc=0, handlelength=2.5)"
            )

        Plt(1, bin2__different_gammas_HQ10000_G1_2_1_005[0], "b")
        Plt(1, bin2_different_gammas_HQ10000_G1_2_3_005[0], "r")
        Plt(1, bin2_different_gammas_HQ10000_G1_2_5_005[0], "g")
        Plt(1, bin2_different_gammas_HQ10000_G1_2_7_005[0], "k")
        Plt(1, bin2_different_gammas_HQ10000_G1_2_9_005[0], "c")
        ax1.set_title(
            r"Time evolution of files = %s, different r bins,\
                      $\gamma = -2.0$"
            % HQ0[:-9],
            fontsize=20,
        )

        Plt(2, bin2_different_gammas_HQ10000_G1_2_1_005[4], "r", HQ12[9:])
        Plt(2, bin2_different_gammas_HQ10000_G1_2_3_005[4], "g", HQ24[9:])
        Plt(2, bin2_different_gammas_HQ10000_G1_2_5_005[4], "k", HQ36[9:])
        Plt(2, bin2_different_gammas_HQ10000_G1_2_7_005[4], "c", HQ48[9:])
        Plt(2, bin2_different_gammas_HQ10000_G1_2_9_005[4], "m", HQ60[9:])

        Plt(3, bin2_different_gammas_HQ10000_G1_2_1_005[0], "r")
        Plt(3, bin2_different_gammas_HQ10000_G1_2_3_005[0], "g")
        Plt(3, bin2_different_gammas_HQ10000_G1_2_5_005[0], "k")
        Plt(3, bin2_different_gammas_HQ10000_G1_2_7_005[0], "c")
        Plt(3, bin2_different_gammas_HQ10000_G1_2_9_005[0], "m")

        Plt(4, bin2_different_gammas_HQ10000_G1_2_1_005[4], "r")
        Plt(4, bin2_different_gammas_HQ10000_G1_2_3_005[4], "g")
        Plt(4, bin2_different_gammas_HQ10000_G1_2_5_005[4], "k")
        Plt(4, bin2_different_gammas_HQ10000_G1_2_7_005[4], "c")
        Plt(4, bin2_different_gammas_HQ10000_G1_2_9_005[4], "m")

        def denom_ax5(a):
            return np.log10(a) * np.exp(-0.5 * a**2)

        d, _ = bin2_different_gammas_HQ10000_G1_2_1_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin2_different_gammas_HQ10000_G1_2_3_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin2_different_gammas_HQ10000_G1_2_5_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin2_different_gammas_HQ10000_G1_2_7_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "c", lw=2, ms=7)
        d, _ = bin2_different_gammas_HQ10000_G1_2_9_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "m", lw=2, ms=7)
        ax5.set_ylim(0, 3)
        ax5.set_ylabel(r"$\frac{f\left( u \right)}{log(x)e^{-0.5x^2}}$", fontsize=20)

        def denom_ax6(a):
            return np.exp(-0.5 * a**2)

        d, _ = bin2_different_gammas_HQ10000_G1_2_1_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin2_different_gammas_HQ10000_G1_2_3_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin2_different_gammas_HQ10000_G1_2_5_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin2_different_gammas_HQ10000_G1_2_7_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "c", lw=2, ms=7)
        d, _ = bin2_different_gammas_HQ10000_G1_2_9_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "m", lw=2, ms=7)
        ax6.set_ylabel(
            r"$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}\
                       {e^{-0.5x^2}}$",
            fontsize=20,
        )

    else:
        ax7.set_xlabel(r"$u_t$", fontsize=20)
        ax7.set_ylabel(r"$\frac{f\left(u \right)}{Tsallis}$", fontsize=20)
        ax8.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax8.set_ylabel(
            r"$\frac{f\left(\log \left(|u_tn|,u_tp \right)\right)}\
                       {Tsallis}$",
            fontsize=20,
        )

    if test2:
        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.set_xticklabels([])")

        for i in range(1, 3):
            exec(
                f"legend(prop=dict(size=13), numpoints=2, ncol=1,\
                          frameon=True, loc=0, handlelength=2.5)"
            )

        Plt(1, bin2_different_gammas_test2_HQ10000_G1_0_0_000[0], "r")
        Plt(1, bin2_different_gammas_test2_HQ10000_G1_0_5_005[0], "g")
        Plt(1, bin2_different_gammas_test2_HQ10000_G1_0_10_005[0], "k")
        Plt(1, bin2_different_gammas_test2_HQ10000_G1_0_15_005[0], "c")
        Plt(1, bin2_different_gammas_test2_HQ10000_G1_0_20_005[0], "m")
        Plt(1, bin2_different_gammas_test2_HQ10000_G1_0_25_005[0], "b")
        ax1.set_title(
            r"Time evolution of files = %s, different r bins,\
                      $\gamma = -2.0$"
            % test2_HQ0[:-9],
            fontsize=20,
        )

        Plt(2, bin2_different_gammas_test2_HQ10000_G1_0_0_000[4], "r", test2_HQ0[15:])
        Plt(2, bin2_different_gammas_test2_HQ10000_G1_0_5_005[4], "g", test2_HQ36[15:])
        Plt(2, bin2_different_gammas_test2_HQ10000_G1_0_10_005[4], "k", test2_HQ66[15:])
        Plt(2, bin2_different_gammas_test2_HQ10000_G1_0_15_005[4], "c", test2_HQ96[15:])
        Plt(
            2, bin2_different_gammas_test2_HQ10000_G1_0_20_005[4], "m", test2_HQ126[15:]
        )
        Plt(
            2, bin2_different_gammas_test2_HQ10000_G1_0_25_005[4], "b", test2_HQ159[15:]
        )

        Plt(3, bin2_different_gammas_test2_HQ10000_G1_0_0_000[0], "r")
        Plt(3, bin2_different_gammas_test2_HQ10000_G1_0_5_005[0], "g")
        Plt(3, bin2_different_gammas_test2_HQ10000_G1_0_10_005[0], "k")
        Plt(3, bin2_different_gammas_test2_HQ10000_G1_0_15_005[0], "c")
        Plt(3, bin2_different_gammas_test2_HQ10000_G1_0_20_005[0], "m")
        Plt(3, bin2_different_gammas_test2_HQ10000_G1_0_25_005[0], "b")

        Plt(4, bin2_different_gammas_test2_HQ10000_G1_0_0_000[4], "r")
        Plt(4, bin2_different_gammas_test2_HQ10000_G1_0_5_005[4], "g")
        Plt(4, bin2_different_gammas_test2_HQ10000_G1_0_10_005[4], "k")
        Plt(4, bin2_different_gammas_test2_HQ10000_G1_0_15_005[4], "c")
        Plt(4, bin2_different_gammas_test2_HQ10000_G1_0_20_005[4], "m")
        Plt(4, bin2_different_gammas_test2_HQ10000_G1_0_25_005[4], "b")

        def denom_ax5(a):
            return 887.569 * a * np.exp(-0.922 * a**2)

        d, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin2_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin2_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin2_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "c", lw=2, ms=7)
        d, _ = bin2_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "m", lw=2, ms=7)
        d, _ = bin2_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "b", lw=2, ms=7)
        ax5.set_ylim(0, 3)
        ax5.set_ylabel(
            r"$\frac{f\left( u \right)}{887.569 \cdot x \cdot\
                       e^{-0.922 \cdot x^2}}$",
            fontsize=20,
        )

        def denom_ax6(a):
            return 3424.993 * (10**a) ** 2 * np.exp(-0.930 * (10**a) ** 2)

        d, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin2_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin2_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin2_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "c", lw=2, ms=7)
        d, _ = bin2_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "m", lw=2, ms=7)
        d, _ = bin2_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "b", lw=2, ms=7)
        ax6.set_ylim(0, 5)
        ax6.set_ylabel(
            r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}\
                       {3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2}}$",
            fontsize=20,
        )

        def denom_ax7(a):
            return (
                864.543
                * a
                * (1 - (1 - 0.946) * 0.908 * a**2) ** (0.946 / (1 - 0.946))
            )

        d, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin2_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin2_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin2_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "c", lw=2, ms=7)
        d, _ = bin2_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "m", lw=2, ms=7)
        d, _ = bin2_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "b", lw=2, ms=7)
        ax7.set_ylim(0, 2)

        def denom_ax8(a):
            return (
                3391.113
                * 10**a
                * (1 - (1 - 0.987) * 0.924 * 10 ** (a**2)) ** (0.987 / (1.0 - 0.987))
            )

        d, _ = bin2_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin2_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin2_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin2_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "c", lw=2, ms=7)
        d, _ = bin2_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "m", lw=2, ms=7)
        d, _ = bin2_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "b", lw=2, ms=7)
        ax8.set_ylim(0, 5)

    if A:
        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.set_xticklabels([])")

        for i in range(1, 7):
            exec(
                f"legend(prop=dict(size=13), numpoints=2, ncol=1,\
                          frameon=True, loc=0, handlelength=2.5)"
            )

        Plt(1, bin2_different_gammas_A_HQ10000_G1_0_0_000[0], "r")
        Plt(1, bin2_different_gammas_A_HQ10000_G1_0_5_005[0], "g")
        Plt(1, bin2_different_gammas_A_HQ10000_G1_0_10_005[0], "k")
        Plt(1, bin2_different_gammas_A_HQ10000_G1_0_40_005[0], "c")
        Plt(1, bin2_different_gammas_A_HQ10000_G1_0_48_009[0], "m")
        Plt(1, bin2_different_gammas_A_HQ10000_G1_0_48_093[0], "b")
        ax1.set_title(
            r"Time evolution of %s, different r bins,\
                      $\gamma = -2.0$"
            % A_HQ0[:-9],
            fontsize=20,
        )

        Plt(2, bin2_different_gammas_A_HQ10000_G1_0_0_000[4], "r", A_HQ0[11:])
        Plt(2, bin2_different_gammas_A_HQ10000_G1_0_5_005[4], "g", A_HQ36[11:])
        Plt(2, bin2_different_gammas_A_HQ10000_G1_0_10_005[4], "k", A_HQ66[11:])
        Plt(2, bin2_different_gammas_A_HQ10000_G1_0_40_005[4], "c", A_HQ246[11:])
        Plt(2, bin2_different_gammas_A_HQ10000_G1_0_48_009[4], "m", A_HQ298[11:])
        Plt(2, bin2_different_gammas_A_HQ10000_G1_0_48_093[4], "b", A_HQ382[11:])

        Plt(3, bin2_different_gammas_A_HQ10000_G1_0_0_000[0], "r")
        Plt(3, bin2_different_gammas_A_HQ10000_G1_0_5_005[0], "g")
        Plt(3, bin2_different_gammas_A_HQ10000_G1_0_10_005[0], "k")
        Plt(3, bin2_different_gammas_A_HQ10000_G1_0_40_005[0], "c")
        Plt(3, bin2_different_gammas_A_HQ10000_G1_0_48_009[0], "m")
        Plt(3, bin2_different_gammas_A_HQ10000_G1_0_48_093[0], "b")

        Plt(4, bin2_different_gammas_A_HQ10000_G1_0_0_000[4], "r")
        Plt(4, bin2_different_gammas_A_HQ10000_G1_0_5_005[4], "g")
        Plt(4, bin2_different_gammas_A_HQ10000_G1_0_10_005[4], "k")
        Plt(4, bin2_different_gammas_A_HQ10000_G1_0_40_005[4], "c")
        Plt(4, bin2_different_gammas_A_HQ10000_G1_0_48_009[4], "m")
        Plt(4, bin2_different_gammas_A_HQ10000_G1_0_48_093[4], "b")

        def denom_ax5(a):
            return 887.569 * a * np.exp(-0.922 * a**2)

        d, _ = bin2_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin2_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin2_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin2_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "c", lw=2, ms=7)
        d, _ = bin2_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "m", lw=2, ms=7)
        d, _ = bin2_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "b", lw=2, ms=7)
        ax5.set_ylim(0.5, 1.5)
        ax5.set_ylabel(
            r"$\frac{f\left( u \right)}{887.569 \cdot x \cdot\
                       e^{-0.922 \cdot x^2}}$",
            fontsize=20,
        )

        def denom_ax6(a):
            return 3424.993 * (10**a) ** 2 * np.exp(-0.930 * (10**a) ** 2)

        d, _ = bin2_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin2_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin2_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin2_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "c", lw=2, ms=7)
        d, _ = bin2_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "m", lw=2, ms=7)
        d, _ = bin2_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "b", lw=2, ms=7)
        ax6.set_ylim(0.5, 1.5)
        ax6.set_ylabel(
            r"$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}\
                       {3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2}}$",
            fontsize=20,
        )

        def denom_ax7(a):
            return (
                864.543
                * a
                * (1 - (1 - 0.946) * 0.908 * a**2) ** (0.946 / (1 - 0.946))
            )

        d, _ = bin2_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin2_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin2_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin2_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "c", lw=2, ms=7)
        d, _ = bin2_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "m", lw=2, ms=7)
        d, _ = bin2_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "b", lw=2, ms=7)
        ax7.set_ylim(0.5, 1.5)

        def denom_ax8(a):
            return (
                3391.113
                * 10**a
                * (1 - (1 - 0.987) * 0.924 * 10 ** (a**2)) ** (0.987 / (1.0 - 0.987))
            )

        d, _ = bin2_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin2_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin2_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin2_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "c", lw=2, ms=7)
        d, _ = bin2_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "m", lw=2, ms=7)
        d, _ = bin2_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "b", lw=2, ms=7)
        ax8.set_ylim(0.5, 1.5)

    if B:
        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.set_xticklabels([])")

        for i in range(1, 7):
            exec(
                f"legend(prop=dict(size=13), numpoints=2, ncol=1,\
                          frameon=True, loc=0, handlelength=2.5)"
            )

        Plt(1, bin2_different_gammas_B_HQ10000_G1_0_0_000[0], "r")
        Plt(1, bin2_different_gammas_B_HQ10000_G1_0_5_005[0], "g")
        Plt(1, bin2_different_gammas_B_HQ10000_G1_0_10_005[0], "k")
        Plt(1, bin2_different_gammas_B_HQ10000_G1_0_198_000[0], "c")
        Plt(1, bin2_different_gammas_B_HQ10000_G1_0_198_093[0], "m")
        ax1.set_title(
            r"Time evolution of %s, different r bins,\
                      $\gamma = -2.0$"
            % B_HQ0[:-9],
            fontsize=20,
        )

        Plt(2, bin2_different_gammas_B_HQ10000_G1_0_0_000[4], "r", B_HQ0[11:])
        Plt(2, bin2_different_gammas_B_HQ10000_G1_0_5_005[4], "g", B_HQ36[11:])
        Plt(2, bin2_different_gammas_B_HQ10000_G1_0_10_005[4], "k", B_HQ66[11:])
        Plt(2, bin2_different_gammas_B_HQ10000_G1_0_198_000[4], "c", B_HQ294[11:])
        Plt(2, bin2_different_gammas_B_HQ10000_G1_0_198_093[4], "m", B_HQ382[11:])

        Plt(3, bin2_different_gammas_B_HQ10000_G1_0_0_000[0], "r")
        Plt(3, bin2_different_gammas_B_HQ10000_G1_0_5_005[0], "g")
        Plt(3, bin2_different_gammas_B_HQ10000_G1_0_10_005[0], "k")
        Plt(3, bin2_different_gammas_B_HQ10000_G1_0_198_000[0], "c")
        Plt(3, bin2_different_gammas_B_HQ10000_G1_0_198_093[0], "m")

        Plt(4, bin2_different_gammas_B_HQ10000_G1_0_0_000[4], "r")
        Plt(4, bin2_different_gammas_B_HQ10000_G1_0_5_005[4], "g")
        Plt(4, bin2_different_gammas_B_HQ10000_G1_0_10_005[4], "k")
        Plt(4, bin2_different_gammas_B_HQ10000_G1_0_198_000[4], "c")
        Plt(4, bin2_different_gammas_B_HQ10000_G1_0_198_093[4], "m")

        def denom_ax5(a):
            return 914.415 * a * np.exp(-0.930 * a**2)

        d, _ = bin2_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin2_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin2_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin2_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "c", lw=2, ms=7)
        d, _ = bin2_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "m", lw=2, ms=7)
        ax5.set_ylim(0, 3)
        ax5.set_ylabel(
            r"$\frac{f\left( u \right)}{914.415 \cdot x \cdot\
                       e^{-0.930 \cdot x^2}}$",
            fontsize=20,
        )

        def denom_ax6(a):
            return 3452.955 * (10**a) ** 2 * np.exp(-0.936 * (10**a) ** 2)

        d, _ = bin2_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin2_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin2_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin2_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "c", lw=2, ms=7)
        d, _ = bin2_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "m", lw=2, ms=7)
        ax6.set_ylim(0, 3)
        ax6.set_ylabel(
            r"$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}\
                       {3452.955 \cdot x^2 \cdot e^{-0.936 \cdot x^2}}$",
            fontsize=20,
        )

        def denom_ax7(a):
            return (
                894.292
                * a
                * (1 - (1 - 0.955) * 0.918 * a**2) ** (0.955 / (1 - 0.955))
            )

        d, _ = bin2_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin2_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin2_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin2_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "c", lw=2, ms=7)
        d, _ = bin2_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "m", lw=2, ms=7)
        ax7.set_ylim(0, 2)

        def denom_ax8(a):
            return (
                3418.569
                * 10**a
                * (1 - (1 - 0.987) * 0.929 * 10 ** (a**2)) ** (0.987 / (1.0 - 0.987))
            )

        d, _ = bin2_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin2_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin2_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin2_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "c", lw=2, ms=7)
        d, _ = bin2_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "m", lw=2, ms=7)
        ax8.set_ylim(0, 5)

if Fig5c_GPerts_gammas_2_5_vt_divided_by_gauss_and_Tsallis:
    f, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(4, 2)

    ax1.set_ylabel(r"$f\left(u\right)$", fontsize=20)
    ax2.set_ylabel(r"$f\left(\log \left( |u_n|,u_p \right)\right)$", fontsize=20)
    ax3.set_ylabel(r"$\log \left( f\left( u \right) \right)$", fontsize=20)
    ax3.set_yscale("log")
    ax4.set_ylabel(
        r"$\log \left( f\left(\log \left( |u_n|,\
                   u_p \right)\right) \right)$",
        fontsize=20,
    )
    ax4.set_yscale("log")

    for i in range(1, 7):
        exec(f"ax{i}.set_xticklabels([])")

    if test:
        for i in range(1, 7):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(
                f"legend(prop=dict(size=13), numpoints=2, ncol=1,\
                          frameon=True, loc=0, handlelength=2.5)"
            )

        Plt(1, bin3_different_gammas_HQ10000_G1_2_1_005[0], "b")
        Plt(1, bin3_different_gammas_HQ10000_G1_2_3_005[0], "r")
        Plt(1, bin3_different_gammas_HQ10000_G1_2_5_005[0], "g")
        Plt(1, bin3_different_gammas_HQ10000_G1_2_7_005[0], "k")
        Plt(1, bin3_different_gammas_HQ10000_G1_2_9_005[0], "c")
        ax1.set_title(
            r"Time evolution of files = %s, different r bins,\
                      $\gamma = -2.5$"
            % HQ0[:-9],
            fontsize=20,
        )

        Plt(2, bin3_different_gammas_HQ10000_G1_2_1_005[4], "r", HQ12[9:])
        Plt(2, bin3_different_gammas_HQ10000_G1_2_3_005[4], "g", HQ24[9:])
        Plt(2, bin3_different_gammas_HQ10000_G1_2_5_005[4], "k", HQ36[9:])
        Plt(2, bin3_different_gammas_HQ10000_G1_2_7_005[4], "c", HQ48[9:])
        Plt(2, bin3_different_gammas_HQ10000_G1_2_9_005[4], "m", HQ60[9:])

        Plt(3, bin3_different_gammas_HQ10000_G1_2_1_005[0], "r")
        Plt(3, bin3_different_gammas_HQ10000_G1_2_3_005[0], "g")
        Plt(3, bin3_different_gammas_HQ10000_G1_2_5_005[0], "k")
        Plt(3, bin3_different_gammas_HQ10000_G1_2_7_005[0], "c")
        Plt(3, bin3_different_gammas_HQ10000_G1_2_9_005[0], "m")

        Plt(4, bin3_different_gammas_HQ10000_G1_2_1_005[4], "r")
        Plt(4, bin3_different_gammas_HQ10000_G1_2_3_005[4], "g")
        Plt(4, bin3_different_gammas_HQ10000_G1_2_5_005[4], "k")
        Plt(4, bin3_different_gammas_HQ10000_G1_2_7_005[4], "c")
        Plt(4, bin3_different_gammas_HQ10000_G1_2_9_005[4], "m")

        def denom_ax5(a):
            return np.log10(a) * np.exp(-0.5 * a**2)

        d, _ = bin3_different_gammas_HQ10000_G1_2_1_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin3_different_gammas_HQ10000_G1_2_3_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin3_different_gammas_HQ10000_G1_2_5_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin3_different_gammas_HQ10000_G1_2_7_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "c", lw=2, ms=7)
        d, _ = bin3_different_gammas_HQ10000_G1_2_9_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "m", lw=2, ms=7)
        ax5.set_ylim(0, 3)
        ax5.set_ylabel(r"$\frac{f\left(u\right)}{log(x)e^{-0.5x^2}}$", fontsize=20)

        def denom_ax6(a):
            return np.exp(-0.5 * a**2)

        d, _ = bin3_different_gammas_HQ10000_G1_2_1_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin3_different_gammas_HQ10000_G1_2_3_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin3_different_gammas_HQ10000_G1_2_5_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin3_different_gammas_HQ10000_G1_2_7_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "c", lw=2, ms=7)
        d, _ = bin3_different_gammas_HQ10000_G1_2_9_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "m", lw=2, ms=7)
        ax6.set_ylabel(
            r"$\frac{f\left(\log \left(|u_n|,u_p \right)\right)}\
                       {e^{-0.5x^2}}$",
            fontsize=20,
        )

    else:
        ax7.set_xlabel(r"$u_t$", fontsize=20)
        ax7.set_ylabel(r"$\frac{f\left(u \right)}{Tsallis}$", fontsize=20)
        ax8.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax8.set_ylabel(
            r"$\frac{f\left(\log \left(|u_tn|,u_tp\
                       \right)\right)}{Tsallis}$",
            fontsize=20,
        )
        for i in range(1, 9):
            exec(f"ax{i}.grid()")

    if test2:
        for i in range(1, 3):
            exec(
                f"legend(prop=dict(size=13), numpoints=2, ncol=1,\
                          frameon=True, loc=0, handlelength=2.5)"
            )

        Plt(1, bin3_different_gammas_test2_HQ10000_G1_0_0_000[0], "r")
        Plt(1, bin3_different_gammas_test2_HQ10000_G1_0_5_005[0], "g")
        Plt(1, bin3_different_gammas_test2_HQ10000_G1_0_10_005[0], "k")
        Plt(1, bin3_different_gammas_test2_HQ10000_G1_0_15_005[0], "c")
        Plt(1, bin3_different_gammas_test2_HQ10000_G1_0_20_005[0], "m")
        Plt(1, bin3_different_gammas_test2_HQ10000_G1_0_25_005[0], "b")
        ax1.set_title(
            r"Time evolution of files = %s, different r bins,\
                      $\gamma = -2.5$"
            % test2_HQ0[:-9],
            fontsize=20,
        )

        Plt(2, bin3_different_gammas_test2_HQ10000_G1_0_0_000[4], "r", test2_HQ0[15:])
        Plt(2, bin3_different_gammas_test2_HQ10000_G1_0_5_005[4], "g", test2_HQ36[15:])
        Plt(2, bin3_different_gammas_test2_HQ10000_G1_0_10_005[4], "k", test2_HQ66[15:])
        Plt(2, bin3_different_gammas_test2_HQ10000_G1_0_15_005[4], "c", test2_HQ96[15:])
        Plt(
            2, bin3_different_gammas_test2_HQ10000_G1_0_20_005[4], "m", test2_HQ126[15:]
        )
        Plt(
            2, bin3_different_gammas_test2_HQ10000_G1_0_25_005[4], "b", test2_HQ159[15:]
        )

        Plt(3, bin3_different_gammas_test2_HQ10000_G1_0_0_000[0], "r")
        Plt(3, bin3_different_gammas_test2_HQ10000_G1_0_5_005[0], "g")
        Plt(3, bin3_different_gammas_test2_HQ10000_G1_0_10_005[0], "k")
        Plt(3, bin3_different_gammas_test2_HQ10000_G1_0_15_005[0], "c")
        Plt(3, bin3_different_gammas_test2_HQ10000_G1_0_20_005[0], "m")
        Plt(3, bin3_different_gammas_test2_HQ10000_G1_0_25_005[0], "b")

        Plt(4, bin3_different_gammas_test2_HQ10000_G1_0_0_000[4], "r")
        Plt(4, bin3_different_gammas_test2_HQ10000_G1_0_5_005[4], "g")
        Plt(4, bin3_different_gammas_test2_HQ10000_G1_0_10_005[4], "k")
        Plt(4, bin3_different_gammas_test2_HQ10000_G1_0_15_005[4], "c")
        Plt(4, bin3_different_gammas_test2_HQ10000_G1_0_20_005[4], "m")
        Plt(4, bin3_different_gammas_test2_HQ10000_G1_0_25_005[4], "b")

        def denom_ax5(a):
            return 887.569 * a * np.exp(-0.922 * a**2)

        d, _ = bin3_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin3_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin3_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin3_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "c", lw=2, ms=7)
        d, _ = bin3_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "m", lw=2, ms=7)
        d, _ = bin3_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "b", lw=2, ms=7)

        ax5.set_ylim(0, 3)
        ax5.set_ylabel(
            r"$\frac{f\left(u \right)}{887.569 \cdot x \cdot\
                       e^{-0.922 \cdot x^2}}$",
            fontsize=20,
        )

        def denom_ax6(a):
            return 3424.993 * (10**a) ** 2 * np.exp(-0.930 * (10**a) ** 2)

        d, _ = bin3_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin3_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin3_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin3_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "c", lw=2, ms=7)
        d, _ = bin3_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "m", lw=2, ms=7)
        d, _ = bin3_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "b", lw=2, ms=7)
        ax6.set_ylim(0, 5)
        ax6.set_ylabel(
            r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\
                       \right)}{3424.993 \cdot x^2 \cdot e^{-0.930\
                       \cdot x^2}}$",
            fontsize=20,
        )

        def denom_ax7(a):
            return (
                864.543
                * a
                * (1 - (1 - 0.946) * 0.908 * a**2) ** (0.946 / (1 - 0.946))
            )

        d, _ = bin3_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin3_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin3_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin3_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "c", lw=2, ms=7)
        d, _ = bin3_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "m", lw=2, ms=7)
        d, _ = bin3_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "b", lw=2, ms=7)
        ax7.set_ylim(0, 2)

        def denom_ax8(a):
            return (
                3391.113
                * 10**a
                * (1 - (1 - 0.987) * 0.924 * 10 ** (a**2)) ** (0.987 / (1.0 - 0.987))
            )

        d, _ = bin3_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin3_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin3_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin3_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "c", lw=2, ms=7)
        d, _ = bin3_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "m", lw=2, ms=7)
        d, _ = bin3_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "b", lw=2, ms=7)
        ax8.set_ylim(0, 5)

    if A:
        for i in range(1, 7):
            exec(
                f"legend(prop=dict(size=13), numpoints=2, ncol=1,\
                          frameon=True, loc=0, handlelength=2.5)"
            )

        Plt(1, bin3_different_gammas_A_HQ10000_G1_0_0_000[0], "r")
        Plt(1, bin3_different_gammas_A_HQ10000_G1_0_5_005[0], "g")
        Plt(1, bin3_different_gammas_A_HQ10000_G1_0_10_005[0], "k")
        Plt(1, bin3_different_gammas_A_HQ10000_G1_0_40_005[0], "c")
        Plt(1, bin3_different_gammas_A_HQ10000_G1_0_48_009[0], "m")
        Plt(1, bin3_different_gammas_A_HQ10000_G1_0_48_093[0], "b")
        ax1.set_title(
            r"Time evolution of %s, different r bins,\
                      $\gamma = -2.5$"
            % A_HQ0[:-9],
            fontsize=20,
        )

        Plt(2, bin3_different_gammas_A_HQ10000_G1_0_0_000[4], "r", A_HQ0[11:])
        Plt(2, bin3_different_gammas_A_HQ10000_G1_0_5_005[4], "g", A_HQ36[11:])
        Plt(2, bin3_different_gammas_A_HQ10000_G1_0_10_005[4], "k", A_HQ66[11:])
        Plt(2, bin3_different_gammas_A_HQ10000_G1_0_40_005[4], "c", A_HQ246[11:])
        Plt(2, bin3_different_gammas_A_HQ10000_G1_0_48_009[4], "m", A_HQ298[11:])
        Plt(2, bin3_different_gammas_A_HQ10000_G1_0_48_093[4], "b", A_HQ382[11:])

        Plt(3, bin3_different_gammas_A_HQ10000_G1_0_0_000[0], "r")
        Plt(3, bin3_different_gammas_A_HQ10000_G1_0_5_005[0], "g")
        Plt(3, bin3_different_gammas_A_HQ10000_G1_0_10_005[0], "k")
        Plt(3, bin3_different_gammas_A_HQ10000_G1_0_40_005[0], "c")
        Plt(3, bin3_different_gammas_A_HQ10000_G1_0_48_009[0], "m")
        Plt(3, bin3_different_gammas_A_HQ10000_G1_0_48_093[0], "b")

        Plt(4, bin3_different_gammas_A_HQ10000_G1_0_0_000[4], "r")
        Plt(4, bin3_different_gammas_A_HQ10000_G1_0_5_005[4], "g")
        Plt(4, bin3_different_gammas_A_HQ10000_G1_0_10_005[4], "k")
        Plt(4, bin3_different_gammas_A_HQ10000_G1_0_40_005[4], "c")
        Plt(4, bin3_different_gammas_A_HQ10000_G1_0_48_009[4], "m")
        Plt(4, bin3_different_gammas_A_HQ10000_G1_0_48_093[4], "b")

        def denom_ax5(a):
            return 887.569 * a * np.exp(-0.922 * a**2)

        d, _ = bin3_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]), "r", lw=2, ms=7)
        d, _ = bin3_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]), "g", lw=2, ms=7)
        d, _ = bin3_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]), "k", lw=2, ms=7)
        d, _ = bin3_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]), "c", lw=2, ms=7)
        d, _ = bin3_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]), "m", lw=2, ms=7)
        d, _ = bin3_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax5.plot(data[:, 0], data[:, 1] / denom_ax5(data[:, 0]), "b", lw=2, ms=7)
        ax5.set_ylim(0.5, 1.5)
        ax5.set_ylabel(
            r"$\frac{f\left( u \right)}{887.569 \cdot x \cdot\
                       e^{-0.922 \cdot x^2}}$",
            fontsize=20,
        )

        def denom_ax6(a):
            return 3424.993 * (10**a) ** 2 * np.exp(-0.930 * (10**a) ** 2)

        d, _ = bin3_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin3_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin3_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin3_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "c", lw=2, ms=7)
        d, _ = bin3_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "m", lw=2, ms=7)
        d, _ = bin3_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "b", lw=2, ms=7)
        ax6.set_ylim(0.5, 1.5)
        ax6.set_ylabel(
            r"$\frac{f\left(\log \left( |u_n|,u_p \right)\
                       \right)}{3424.993 \cdot x^2 \cdot e^{-0.930\
                       \cdot x^2 }}$",
            fontsize=20,
        )

        def denom_ax7(a):
            return (
                864.543
                * a
                * (1 - (1 - 0.946) * 0.908 * a**2) ** (0.946 / (1 - 0.946))
            )

        d, _ = bin3_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin3_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin3_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin3_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "c", lw=2, ms=7)
        d, _ = bin3_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "m", lw=2, ms=7)
        d, _ = bin3_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "b", lw=2, ms=7)
        ax7.set_ylim(0.5, 1.5)

        def denom_ax8(a):
            return (
                3391.113
                * 10**a
                * (1 - (1 - 0.987) * 0.924 * 10 ** (a**2)) ** (0.987 / (1.0 - 0.987))
            )

        d, _ = bin3_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin3_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin3_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin3_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "c", lw=2, ms=7)
        d, _ = bin3_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "m", lw=2, ms=7)
        d, _ = bin3_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "b", lw=2, ms=7)
        ax8.set_ylim(0.5, 1.5)

    if B:
        for i in range(1, 7):
            exec(
                f"legend(prop=dict(size=13), numpoints=2, ncol=1,\
                          frameon=True, loc=0, handlelength=2.5)"
            )

        Plt(1, bin3_different_gammas_B_HQ10000_G1_0_0_000[0], "r")
        Plt(1, bin3_different_gammas_B_HQ10000_G1_0_5_005[0], "g")
        Plt(1, bin3_different_gammas_B_HQ10000_G1_0_10_005[0], "k")
        Plt(1, bin3_different_gammas_B_HQ10000_G1_0_198_000[0], "c")
        Plt(1, bin3_different_gammas_B_HQ10000_G1_0_198_093[0], "m")
        ax1.set_title(
            r"Time evolution of %s, different r bins,\
                      $\gamma = -2.5$"
            % B_HQ0[:-9],
            fontsize=20,
        )

        Plt(2, bin3_different_gammas_B_HQ10000_G1_0_0_000[4], "r", B_HQ0[11:])
        Plt(2, bin3_different_gammas_B_HQ10000_G1_0_5_005[4], "g", B_HQ36[11:])
        Plt(2, bin3_different_gammas_B_HQ10000_G1_0_10_005[4], "k", B_HQ66[11:])
        Plt(2, bin3_different_gammas_B_HQ10000_G1_0_198_000[4], "c", B_HQ294[11:])
        Plt(2, bin3_different_gammas_B_HQ10000_G1_0_198_093[4], "m", B_HQ382[11:])

        Plt(3, bin3_different_gammas_B_HQ10000_G1_0_0_000[0], "r")
        Plt(3, bin3_different_gammas_B_HQ10000_G1_0_5_005[0], "g")
        Plt(3, bin3_different_gammas_B_HQ10000_G1_0_10_005[0], "k")
        Plt(3, bin3_different_gammas_B_HQ10000_G1_0_198_000[0], "c")
        Plt(3, bin3_different_gammas_B_HQ10000_G1_0_198_093[0], "m")

        Plt(4, bin3_different_gammas_B_HQ10000_G1_0_0_000[4], "r")
        Plt(4, bin3_different_gammas_B_HQ10000_G1_0_5_005[4], "g")
        Plt(4, bin3_different_gammas_B_HQ10000_G1_0_10_005[4], "k")
        Plt(4, bin3_different_gammas_B_HQ10000_G1_0_198_000[4], "c")
        Plt(4, bin3_different_gammas_B_HQ10000_G1_0_198_093[4], "m")

        def denom_ax5(a):
            return 914.415 * a * np.exp(-0.930 * a**2)

        d, _ = bin3_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin3_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin3_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin3_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "c", lw=2, ms=7)
        d, _ = bin3_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "m", lw=2, ms=7)
        ax5.set_ylim(0, 3)
        ax5.set_ylabel(
            r"$\frac{f\left( u \right)}{914.415 \cdot x \cdot\
                       e^{-0.930 \cdot x^2}}$",
            fontsize=20,
        )

        def denom_ax6(a):
            return 3452.955 * (10**a) ** 2 * np.exp(-0.936 * (10**a) ** 2)

        d, _ = bin3_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin3_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin3_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin3_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "c", lw=2, ms=7)
        d, _ = bin3_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "m", lw=2, ms=7)
        ax6.set_ylim(0, 3)
        ax6.set_ylabel(
            r"$\frac{f\left(\log \left( |u_n|,\
                       u_p \right)\right)}{3452.955 \cdot x^2\
                       \cdot e^{-0.936 \cdot x^2}}$",
            fontsize=20,
        )

        def denom_ax7(a):
            return (
                894.292
                * a
                * (1 - (1 - 0.955) * 0.918 * a**2) ** (0.955 / (1 - 0.955))
            )

        d, _ = bin3_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin3_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin3_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin3_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "c", lw=2, ms=7)
        d, _ = bin3_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "m", lw=2, ms=7)
        ax7.set_ylim(0, 2)

        def denom_ax8(a):
            return (
                3418.569
                * 10**a
                * (1 - (1 - 0.987) * 0.929 * 10 ** (a**2)) ** (0.987 / (1.0 - 0.987))
            )

        d, _ = bin3_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin3_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin3_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin3_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "c", lw=2, ms=7)
        d, _ = bin3_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "m", lw=2, ms=7)
        ax8.set_ylim(0, 5)

if Fig5d_GPerts_gammas_3_0_vt_divided_by_gauss_and_Tsallis:
    f, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(4, 2)

    for i in range(1, 7):
        exec(f"ax{i}.set_xticklabels([])")

    ax1.set_ylabel(r"$f\left(u \right)$", fontsize=20)
    ax2.set_ylabel(r"$f\left(\log\left(|u_n|,u_p\right)\right)$", fontsize=20)
    ax3.set_ylabel(r"$\log \left( f\left( u \right) \right)$", fontsize=20)
    ax3.set_yscale("log")
    ax4.set_ylabel(
        r"$\log\left(f\left(\log\left(|u_n|,u_p\right)\
                   \right)\right)$",
        fontsize=20,
    )
    ax4.set_yscale("log")

    if test:
        for i in range(1, 7):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(
                f"legend(prop=dict(size=13), numpoints=2, ncol=1,\
                          frameon=True, loc=0, handlelength=2.5)"
            )

        Plt(1, bin4_different_gammas_HQ10000_G1_2_1_005[0], "b")
        Plt(1, bin4_different_gammas_HQ10000_G1_2_3_005[0], "r")
        Plt(1, bin4_different_gammas_HQ10000_G1_2_5_005[0], "g")
        Plt(1, bin4_different_gammas_HQ10000_G1_2_7_005[0], "k")
        Plt(1, bin4_different_gammas_HQ10000_G1_2_9_005[0], "m")
        ax1.set_title(
            r"Time evolution of files = %s, different r bins,\
                      $\gamma = -3.0$"
            % HQ0[:-9],
            fontsize=20,
        )

        Plt(2, bin4_different_gammas_HQ10000_G1_2_1_005[4], "r", HQ12[9:])
        Plt(2, bin4_different_gammas_HQ10000_G1_2_3_005[4], "g", HQ24[9:])
        Plt(2, bin4_different_gammas_HQ10000_G1_2_5_005[4], "k", HQ36[9:])
        Plt(2, bin4_different_gammas_HQ10000_G1_2_7_005[4], "c", HQ48[9:])
        Plt(2, bin4_different_gammas_HQ10000_G1_2_9_005[4], "m", HQ60[9:])

        Plt(3, bin4_different_gammas_HQ10000_G1_2_1_005[0], "r")
        Plt(3, bin4_different_gammas_HQ10000_G1_2_3_005[0], "g")
        Plt(3, bin4_different_gammas_HQ10000_G1_2_5_005[0], "k")
        Plt(3, bin4_different_gammas_HQ10000_G1_2_7_005[0], "c")
        Plt(3, bin4_different_gammas_HQ10000_G1_2_9_005[0], "m")

        Plt(4, bin4_different_gammas_HQ10000_G1_2_1_005[4], "r")
        Plt(4, bin4_different_gammas_HQ10000_G1_2_3_005[4], "g")
        Plt(4, bin4_different_gammas_HQ10000_G1_2_5_005[4], "k")
        Plt(4, bin4_different_gammas_HQ10000_G1_2_7_005[4], "c")
        Plt(4, bin4_different_gammas_HQ10000_G1_2_9_005[4], "m")

        def denom_ax5(a):
            return np.log10(a) * np.exp(-0.5 * a**2)

        d, _ = bin4_different_gammas_HQ10000_G1_2_1_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin4_different_gammas_HQ10000_G1_2_3_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin4_different_gammas_HQ10000_G1_2_5_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin4_different_gammas_HQ10000_G1_2_7_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "c", lw=2, ms=7)
        d, _ = bin4_different_gammas_HQ10000_G1_2_9_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "m", lw=2, ms=7)
        ax5.set_ylim(0, 3)
        ax5.set_ylabel(r"$\frac{f\left( u \right)}{log(x)e^{-0.5x^2}}$", fontsize=20)

        def denom_ax6(a):
            return np.exp(-0.5 * a**2)

        d, _ = bin4_different_gammas_HQ10000_G1_2_1_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin4_different_gammas_HQ10000_G1_2_3_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin4_different_gammas_HQ10000_G1_2_5_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin4_different_gammas_HQ10000_G1_2_7_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "c", lw=2, ms=7)
        d, _ = bin4_different_gammas_HQ10000_G1_2_9_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "m", lw=2, ms=7)
        ax6.set_ylabel(
            r"$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}\
                       {e^{-0.5x^2}}$",
            fontsize=20,
        )

    else:
        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        ax8.set_xlabel(r"$\log\left(|u_tn|,u_tp\right)$", fontsize=20)
        ax8.set_ylabel(
            r"$\frac{f\left(\log\left(|u_tn|,u_tp\right)\
                       \right)}{Tsallis}$",
            fontsize=20,
        )

    if test2:
        for i in range(1, 3):
            exec(
                f"legend(prop=dict(size=13), numpoints=2, ncol=1,\
                          frameon=True, loc=0, handlelength=2.5)"
            )

        Plt(1, bin4_different_gammas_test2_HQ10000_G1_0_0_000[0], "r")
        Plt(1, bin4_different_gammas_test2_HQ10000_G1_0_5_005[0], "g")
        Plt(1, bin4_different_gammas_test2_HQ10000_G1_0_10_005[0], "k")
        Plt(1, bin4_different_gammas_test2_HQ10000_G1_0_15_005[0], "c")
        Plt(1, bin4_different_gammas_test2_HQ10000_G1_0_20_005[0], "m")
        Plt(1, bin4_different_gammas_test2_HQ10000_G1_0_25_005[0], "b")
        ax1.set_title(
            r"Time evolution of files = %s, different r bins,\
                      $\gamma = -3.0$"
            % test2_HQ0[:-9],
            fontsize=20,
        )

        Plt(2, bin4_different_gammas_test2_HQ10000_G1_0_0_000[4], "r", test2_HQ0[15:])
        Plt(2, bin4_different_gammas_test2_HQ10000_G1_0_5_005[4], "g", test2_HQ36[15:])
        Plt(2, bin4_different_gammas_test2_HQ10000_G1_0_10_005[4], "k", test2_HQ66[15:])
        Plt(2, bin4_different_gammas_test2_HQ10000_G1_0_15_005[4], "c", test2_HQ96[15:])
        Plt(
            2, bin4_different_gammas_test2_HQ10000_G1_0_20_005[4], "m", test2_HQ126[15:]
        )
        Plt(
            2, bin4_different_gammas_test2_HQ10000_G1_0_25_005[4], "b", test2_HQ159[15:]
        )

        Plt(3, bin4_different_gammas_test2_HQ10000_G1_0_0_000[0], "r")
        Plt(3, bin4_different_gammas_test2_HQ10000_G1_0_5_005[0], "g")
        Plt(3, bin4_different_gammas_test2_HQ10000_G1_0_10_005[0], "k")
        Plt(3, bin4_different_gammas_test2_HQ10000_G1_0_15_005[0], "c")
        Plt(3, bin4_different_gammas_test2_HQ10000_G1_0_20_005[0], "m")
        Plt(3, bin4_different_gammas_test2_HQ10000_G1_0_25_005[0], "b")

        Plt(4, bin4_different_gammas_test2_HQ10000_G1_0_0_000[4], "r")
        Plt(4, bin4_different_gammas_test2_HQ10000_G1_0_5_005[4], "g")
        Plt(4, bin4_different_gammas_test2_HQ10000_G1_0_10_005[4], "k")
        Plt(4, bin4_different_gammas_test2_HQ10000_G1_0_15_005[4], "c")
        Plt(4, bin4_different_gammas_test2_HQ10000_G1_0_20_005[4], "m")
        Plt(4, bin4_different_gammas_test2_HQ10000_G1_0_25_005[4], "b")

        def denom_ax5(a):
            return 887.569 * a * np.exp(-0.922 * a**2)

        d, _ = bin4_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin4_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin4_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin4_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "c", lw=2, ms=7)
        d, _ = bin4_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "m", lw=2, ms=7)
        d, _ = bin4_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "b", lw=2, ms=7)
        ax5.set_ylim(0, 3)
        ax5.set_ylabel(
            r"$\frac{f\left( u \right)}{887.569 \cdot x \cdot\
                       e^{-0.922 \cdot x^2}}$",
            fontsize=20,
        )

        def denom_ax6(a):
            return 3424.993 * (10**a) ** 2 * np.exp(-0.930 * (10**a) ** 2)

        d, _ = bin4_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin4_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin4_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin4_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "c", lw=2, ms=7)
        d, _ = bin4_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "m", lw=2, ms=7)
        d, _ = bin4_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "b", lw=2, ms=7)
        ax6.set_ylim(0, 5)
        ax6.set_ylabel(
            r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}\
                       {3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2}}$",
            fontsize=20,
        )

        def denom_ax7(a):
            return (
                864.543
                * a
                * (1 - (1 - 0.946) * 0.908 * a**2) ** (0.946 / (1 - 0.946))
            )

        d, _ = bin4_different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin4_different_gammas_test2_HQ10000_G1_0_5_005[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin4_different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin4_different_gammas_test2_HQ10000_G1_0_15_005[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "c", lw=2, ms=7)
        d, _ = bin4_different_gammas_test2_HQ10000_G1_0_20_005[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "m", lw=2, ms=7)
        d, _ = bin4_different_gammas_test2_HQ10000_G1_0_25_005[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "b", lw=2, ms=7)
        ax7.set_ylim(0, 2)
        ax7.set_xlabel(r"$u_t$", fontsize=20)
        ax7.set_ylabel(r"$\frac{f\left(u\right)}{Tsallis}$", fontsize=20)

        def denom_ax8(a):
            return (
                3391.113
                * 10**a
                * (1 - (1 - 0.987) * 0.924 * 10 ** (a**2)) ** (0.987 / (1.0 - 0.987))
            )

        d, _ = bin4_different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin4_different_gammas_test2_HQ10000_G1_0_5_005[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin4_different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin4_different_gammas_test2_HQ10000_G1_0_15_005[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "c", lw=2, ms=7)
        d, _ = bin4_different_gammas_test2_HQ10000_G1_0_20_005[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "m", lw=2, ms=7)
        d, _ = bin4_different_gammas_test2_HQ10000_G1_0_25_005[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "b", lw=2, ms=7)
        ax8.set_ylim(0, 5)

    if A:
        for i in range(1, 7):
            exec(
                f"legend(prop=dict(size=13), numpoints=2, ncol=1,\
                          frameon=True, loc=0, handlelength=2.5)"
            )

        Plt(1, bin4_different_gammas_A_HQ10000_G1_0_0_000[0], "r")
        Plt(1, bin4_different_gammas_A_HQ10000_G1_0_5_005[0], "g")
        Plt(1, bin4_different_gammas_A_HQ10000_G1_0_10_005[0], "k")
        Plt(1, bin4_different_gammas_A_HQ10000_G1_0_40_005[0], "c")
        Plt(1, bin4_different_gammas_A_HQ10000_G1_0_48_009[0], "m")
        Plt(1, bin4_different_gammas_A_HQ10000_G1_0_48_093[0], "b")
        ax1.set_title(
            r"Time evolution of %s, different r bins,\
                      $\gamma = -3.0$"
            % A_HQ0[:-9],
            fontsize=20,
        )

        Plt(2, bin4_different_gammas_A_HQ10000_G1_0_0_000[4], "r", A_HQ0[11:])
        Plt(2, bin4_different_gammas_A_HQ10000_G1_0_5_005[4], "g", A_HQ36[11:])
        Plt(2, bin4_different_gammas_A_HQ10000_G1_0_10_005[4], "k", A_HQ66[11:])
        Plt(2, bin4_different_gammas_A_HQ10000_G1_0_40_005[4], "c", A_HQ246[11:])
        Plt(2, bin4_different_gammas_A_HQ10000_G1_0_48_009[4], "m", A_HQ298[11:])
        Plt(2, bin4_different_gammas_A_HQ10000_G1_0_48_093[4], "b", A_HQ382[11:])

        Plt(3, bin4_different_gammas_A_HQ10000_G1_0_0_000[0], "r")
        Plt(3, bin4_different_gammas_A_HQ10000_G1_0_5_005[0], "g")
        Plt(3, bin4_different_gammas_A_HQ10000_G1_0_10_005[0], "k")
        Plt(3, bin4_different_gammas_A_HQ10000_G1_0_40_005[0], "c")
        Plt(3, bin4_different_gammas_A_HQ10000_G1_0_48_009[0], "m")
        Plt(3, bin4_different_gammas_A_HQ10000_G1_0_48_093[0], "b")

        Plt(4, bin4_different_gammas_A_HQ10000_G1_0_0_000[4], "r")
        Plt(4, bin4_different_gammas_A_HQ10000_G1_0_5_005[4], "g")
        Plt(4, bin4_different_gammas_A_HQ10000_G1_0_10_005[4], "k")
        Plt(4, bin4_different_gammas_A_HQ10000_G1_0_40_005[4], "c")
        Plt(4, bin4_different_gammas_A_HQ10000_G1_0_48_009[4], "m")
        Plt(4, bin4_different_gammas_A_HQ10000_G1_0_48_093[4], "b")

        def denom_ax5(a):
            return 887.569 * a * np.exp(-0.922 * a**2)

        d, _ = bin4_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin4_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin4_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin4_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "c", lw=2, ms=7)
        d, _ = bin4_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "m", lw=2, ms=7)
        d, _ = bin4_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "b", lw=2, ms=7)
        ax5.set_ylim(0.5, 1.5)
        ax5.set_ylabel(
            r"$\frac{f\left( u \right)}{887.569 \cdot x \cdot\
                       e^{-0.922 \cdot x^2}}$",
            fontsize=20,
        )

        def denom_ax6(a):
            return 3424.993 * (10**a) ** 2 * np.exp(-0.930 * (10**a) ** 2)

        d, _ = bin4_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin4_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin4_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin4_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "c", lw=2, ms=7)
        d, _ = bin4_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "m", lw=2, ms=7)
        d, _ = bin4_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "b", lw=2, ms=7)
        ax6.set_ylim(0.5, 1.5)
        ax6.set_ylabel(
            r"$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}\
                       {3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2}}$",
            fontsize=20,
        )

        def denom_ax7(a):
            return (
                864.543
                * a
                * (1 - (1 - 0.946) * 0.908 * a**2) ** (0.946 / (1 - 0.946))
            )

        d, _ = bin4_different_gammas_A_HQ10000_G1_0_0_000[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin4_different_gammas_A_HQ10000_G1_0_5_005[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin4_different_gammas_A_HQ10000_G1_0_10_005[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin4_different_gammas_A_HQ10000_G1_0_40_005[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "c", lw=2, ms=7)
        d, _ = bin4_different_gammas_A_HQ10000_G1_0_48_009[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "m", lw=2, ms=7)
        d, _ = bin4_different_gammas_A_HQ10000_G1_0_48_093[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "b", lw=2, ms=7)
        ax7.set_ylim(0.5, 1.5)
        ax7.set_xlabel(r"$u_t$", fontsize=20)
        ax7.set_ylabel(r"$\frac{f\left(u\right)}{Tsallis}$", fontsize=20)

        def denom_ax8(a):
            return (
                3391.113
                * 10**a
                * (1 - (1 - 0.987) * 0.924 * 10 ** (a**2)) ** (0.987 / (1.0 - 0.987))
            )

        d, _ = bin4_different_gammas_A_HQ10000_G1_0_0_000[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin4_different_gammas_A_HQ10000_G1_0_5_005[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin4_different_gammas_A_HQ10000_G1_0_10_005[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin4_different_gammas_A_HQ10000_G1_0_40_005[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "c", lw=2, ms=7)
        d, _ = bin4_different_gammas_A_HQ10000_G1_0_48_009[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "m", lw=2, ms=7)
        d, _ = bin4_different_gammas_A_HQ10000_G1_0_48_093[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "b", lw=2, ms=7)
        ax8.set_ylim(0.5, 1.5)

    if B:
        for i in range(1, 7):
            exec(
                f"legend(prop=dict(size=13), numpoints=2, ncol=1,\
                          frameon=True, loc=0, handlelength=2.5)"
            )

        Plt(1, bin4_different_gammas_B_HQ10000_G1_0_0_000[0], "r")
        Plt(1, bin4_different_gammas_B_HQ10000_G1_0_5_005[0], "g")
        Plt(1, bin4_different_gammas_B_HQ10000_G1_0_10_005[0], "k")
        Plt(1, bin4_different_gammas_B_HQ10000_G1_0_198_000[0], "b")
        Plt(1, bin4_different_gammas_B_HQ10000_G1_0_198_093[0], "m")
        ax1.set_title(
            r"Time evolution of %s, different r bins,\
                      $\gamma=-3.0$"
            % B_HQ0[:-9],
            fontsize=20,
        )

        Plt(2, bin4_different_gammas_B_HQ10000_G1_0_0_000[4], "r", B_HQ0[11:])
        Plt(2, bin4_different_gammas_B_HQ10000_G1_0_5_005[4], "g", B_HQ36[11:])
        Plt(2, bin4_different_gammas_B_HQ10000_G1_0_10_005[4], "k", B_HQ66[11:])
        Plt(2, bin4_different_gammas_B_HQ10000_G1_0_198_000[4], "b", B_HQ294[11:])
        Plt(2, bin4_different_gammas_B_HQ10000_G1_0_198_093[4], "m", B_HQ382[11:])

        Plt(3, bin4_different_gammas_B_HQ10000_G1_0_0_000[0], "r")
        Plt(3, bin4_different_gammas_B_HQ10000_G1_0_5_005[0], "g")
        Plt(3, bin4_different_gammas_B_HQ10000_G1_0_10_005[0], "k")
        Plt(3, bin4_different_gammas_B_HQ10000_G1_0_198_000[0], "b")
        Plt(3, bin4_different_gammas_B_HQ10000_G1_0_198_093[0], "m")

        Plt(4, bin4_different_gammas_B_HQ10000_G1_0_0_000[4], "r")
        Plt(4, bin4_different_gammas_B_HQ10000_G1_0_5_005[4], "g")
        Plt(4, bin4_different_gammas_B_HQ10000_G1_0_10_005[4], "k")
        Plt(4, bin4_different_gammas_B_HQ10000_G1_0_198_000[4], "b")
        Plt(4, bin4_different_gammas_B_HQ10000_G1_0_198_093[4], "m")

        def denom_ax5(a):
            return 914.415 * a * np.exp(-0.930 * a**2)

        d, _ = bin4_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin4_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin4_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin4_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "b", lw=2, ms=7)
        d, _ = bin4_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "m", lw=2, ms=7)
        ax5.set_ylim(0, 3)
        ax5.set_ylabel(
            r"$\frac{f\left( u \right)}{914.415 \cdot x \cdot\
                       e^{-0.930 \cdot x^2}}$",
            fontsize=20,
        )

        def denom_ax6(a):
            return 3452.955 * (10**a) ** 2 * np.exp(-0.936 * (10**a) ** 2)

        d, _ = bin4_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin4_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin4_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin4_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "b", lw=2, ms=7)
        d, _ = bin4_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "m", lw=2, ms=7)
        ax6.set_ylim(0, 3)
        ax6.set_ylabel(
            r"$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}\
                       {3452.955 \cdot x^2 \cdot e^{-0.936 \cdot x^2 }}$",
            fontsize=20,
        )

        def denom_ax7(a):
            return (
                894.292
                * a
                * (1 - (1 - 0.955) * 0.918 * a**2) ** (0.955 / (1 - 0.955))
            )

        d, _ = bin4_different_gammas_B_HQ10000_G1_0_0_000[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin4_different_gammas_B_HQ10000_G1_0_5_005[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin4_different_gammas_B_HQ10000_G1_0_10_005[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin4_different_gammas_B_HQ10000_G1_0_198_000[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "b", lw=2, ms=7)
        d, _ = bin4_different_gammas_B_HQ10000_G1_0_198_093[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "m", lw=2, ms=7)
        ax7.set_ylim(0, 2)
        ax7.set_xlabel(r"$u_t$", fontsize=20)
        ax7.set_ylabel(r"$\frac{f\left(u\right)}{Tsallis}$", fontsize=20)

        def denom_ax8(a):
            return (
                3418.569
                * 10**a
                * (1 - (1 - 0.987) * 0.929 * 10 ** (a**2)) ** (0.987 / (1.0 - 0.987))
            )

        d, _ = bin4_different_gammas_B_HQ10000_G1_0_0_000[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin4_different_gammas_B_HQ10000_G1_0_5_005[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin4_different_gammas_B_HQ10000_G1_0_10_005[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin4_different_gammas_B_HQ10000_G1_0_198_000[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "b", lw=2, ms=7)
        d, _ = bin4_different_gammas_B_HQ10000_G1_0_198_093[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "m", lw=2, ms=7)
        ax8.set_ylim(0, 5)

# datalist_bin5different_gammas_test2_HQ10000_G1_0_25_005


def denom_ax5(a):
    return 887.569 * a * np.exp(-0.922 * a**2)


def denom_ax6(a):
    return 3424.993 * (10**a) ** 2 * np.exp(-0.930 * (10**a) ** 2)


def denom_ax7(a):
    return 864.543 * a * (1 - (1 - 0.946) * 0.908 * a**2) ** (0.946 / (1 - 0.946))


def denom_ax8(a):
    return (
        3391.113
        * 10**a
        * (1 - (1 - 0.987) * 0.924 * 10 ** (a**2)) ** (0.987 / (1.0 - 0.987))
    )


if Fig6a_GPerts_R_middle_19_95_vt_divided_by_gauss_and_Tsallis:
    f, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(4, 2)
    if test:
        for i in range(1, 7):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.set_xticklabels([])")

        for i in range(1, 7):
            exec(
                f"legend(prop=dict(size=13), numpoints=2, ncol=1,\
                          frameon=True, loc=0, handlelength=2.5)"
            )

        Plt(1, bin1_different_gammas_HQ10000_G1_2_1_005[0], "b")
        Plt(1, bin1_different_gammas_HQ10000_G1_2_3_005[0], "r")
        Plt(1, bin1_different_gammas_HQ10000_G1_2_5_005[0], "g")
        Plt(1, bin1_different_gammas_HQ10000_G1_2_7_005[0], "k")
        Plt(1, bin1_different_gammas_HQ10000_G1_2_9_005[0], "m")
        ax1.set_ylabel(r"$f\left( u \right)$", fontsize=20)
        ax1.set_title(
            r"Time evolution of files = %s, different r bins,\
                      $\gamma = -1.5$"
            % HQ0[:-9],
            fontsize=20,
        )

        Plt(2, bin1_different_gammas_HQ10000_G1_2_1_005[4], "r", HQ12[9:])
        Plt(2, bin1_different_gammas_HQ10000_G1_2_3_005[4], "g", HQ24[9:])
        Plt(2, bin1_different_gammas_HQ10000_G1_2_5_005[4], "k", HQ36[9:])
        Plt(2, bin1_different_gammas_HQ10000_G1_2_7_005[4], "b", HQ48[9:])
        Plt(2, bin1_different_gammas_HQ10000_G1_2_9_005[4], "m", HQ60[9:])
        ax2.set_ylabel(r"$f\left(\log \left( |u_n|,u_p \right)\right)$", fontsize=20)

        Plt(3, bin1_different_gammas_HQ10000_G1_2_1_005[0], "r")
        Plt(3, bin1_different_gammas_HQ10000_G1_2_3_005[0], "g")
        Plt(3, bin1_different_gammas_HQ10000_G1_2_5_005[0], "k")
        Plt(3, bin1_different_gammas_HQ10000_G1_2_7_005[0], "b")
        Plt(3, bin1_different_gammas_HQ10000_G1_2_9_005[0], "m")
        ax3.set_ylabel(r"$\log \left( f\left( u \right) \right)$", fontsize=20)
        ax3.set_yscale("log")

        Plt(4, bin1_different_gammas_HQ10000_G1_2_1_005[4], "r")
        Plt(4, bin1_different_gammas_HQ10000_G1_2_3_005[4], "g")
        Plt(4, bin1_different_gammas_HQ10000_G1_2_5_005[4], "k")
        Plt(4, bin1_different_gammas_HQ10000_G1_2_7_005[4], "b")
        Plt(4, bin1_different_gammas_HQ10000_G1_2_9_005[4], "m")
        ax4.set_ylabel(
            r"$\log \left( f\left(\log \left(|u_n|,u_p \right)\
                       \right) \right)$",
            fontsize=20,
        )
        ax4.set_yscale("log")

        def denom_ax5(a):
            return np.log10(a) * np.exp(-0.5 * a**2)

        d, _ = bin1_different_gammas_HQ10000_G1_2_1_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin1_different_gammas_HQ10000_G1_2_3_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin1_different_gammas_HQ10000_G1_2_5_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin1_different_gammas_HQ10000_G1_2_7_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "b", lw=2, ms=7)
        d, _ = bin1_different_gammas_HQ10000_G1_2_9_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "m", lw=2, ms=7)
        ax5.set_ylabel(r"$\frac{f\left(u\right)}{log(x)e^{-0.5x^2}}$", fontsize=20)

        def denom_ax6(a):
            return np.exp(-0.5 * a**2)

        d, _ = bin1_different_gammas_HQ10000_G1_2_1_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "r", lw=2, ms=7)
        d, _ = bin1_different_gammas_HQ10000_G1_2_3_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "g", lw=2, ms=7)
        d, _ = bin1_different_gammas_HQ10000_G1_2_5_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "k", lw=2, ms=7)
        d, _ = bin1_different_gammas_HQ10000_G1_2_7_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "b", lw=2, ms=7)
        d, _ = bin1_different_gammas_HQ10000_G1_2_9_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "m", lw=2, ms=7)
        ax6.set_ylabel(
            r"$\frac{f\left(\log \left( |u_n|,u_p \right)\right)}\
                       {e^{-0.5x^2}}$",
            fontsize=20,
        )

    else:
        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        for i in range(1, 3):
            exec(
                f"legend(prop=dict(size=13), numpoints=2, ncol=1,\
                          frameon=True, loc=0, handlelength=2.5)"
            )

        ax1.set_ylabel(r"$f\left(u_t\right)$", fontsize=20)
        ax2.set_ylabel(r"$f\left(\log \left( |u_n|,u_p \right)\right)$", fontsize=20)
        ax3.set_ylabel(r"$\log \left( f\left( u \right) \right)$", fontsize=20)
        ax3.set_yscale("log")
        ax4.set_ylabel(
            r"$\log \left( f\left(\log \left( |u_n|,u_p \right)\
                       \right) \right)$",
            fontsize=20,
        )
        ax4.set_yscale("log")
        ax5.set_ylabel(
            r"$\frac{f\left( u \right)}{887.569 \cdot x \cdot\
                       e^{-0.922 \cdot x^2}}$",
            fontsize=20,
        )
        ax6.set_ylim(0, 5)
        ax6.set_ylabel(
            r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\
                       \right)}{3424.993 \cdot x^2 \cdot\
                       e^{-0.930 \cdot x^2 }}$",
            fontsize=20,
        )
        ax7.set_ylim(0, 2)
        ax7.set_xlabel(r"$u_t$", fontsize=20)
        ax7.set_ylabel(r"$\frac{f\left(u \right)}{Tsallis}$", fontsize=20)
        ax8.set_ylim(0, 5)
        ax8.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax8.set_ylabel(
            r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}\
                       {Tsallis}$",
            fontsize=20,
        )

    if test2:
        ax1.set_title(
            r"Time evolution of files = %s, $R_{middle} = 19.95$" % test2_HQ0[:-9],
            fontsize=20,
        )

        Plt(1, datalist_bin5different_gammas_test2_HQ10000_G1_0_0_000[0], "r")
        Plt(1, datalist_bin5different_gammas_test2_HQ10000_G1_0_10_005[0], "k")
        Plt(1, datalist_bin5different_gammas_test2_HQ10000_G1_0_18_053[0], "b")

        Plt(
            2,
            datalist_bin5different_gammas_test2_HQ10000_G1_0_0_000[4],
            "r",
            test2_HQ0[15:],
        )
        Plt(
            2,
            datalist_bin5different_gammas_test2_HQ10000_G1_0_10_005[4],
            "k",
            test2_HQ66[15:],
        )
        Plt(
            2,
            datalist_bin5different_gammas_test2_HQ10000_G1_0_18_053[4],
            "b",
            test2_HQ166[15:],
        )

        Plt(3, datalist_bin5different_gammas_test2_HQ10000_G1_0_0_000[0], "r")
        Plt(3, datalist_bin5different_gammas_test2_HQ10000_G1_0_10_005[0], "k")
        Plt(3, datalist_bin5different_gammas_test2_HQ10000_G1_0_18_053[0], "b")

        Plt(4, datalist_bin5different_gammas_test2_HQ10000_G1_0_0_000[4], "r")
        Plt(4, datalist_bin5different_gammas_test2_HQ10000_G1_0_10_005[4], "k")
        Plt(4, datalist_bin5different_gammas_test2_HQ10000_G1_0_18_053[4], "b")

        d, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "r", lw=2, ms=7)
        d, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "k", lw=2, ms=7)
        d, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_18_053[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "b", lw=2, ms=7)

        d, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "r", lw=2, ms=7)
        d, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "k", lw=2, ms=7)
        d, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_18_053[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "b", lw=2, ms=7)

        d, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "r", lw=2, ms=7)
        d, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "k", lw=2, ms=7)
        d, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_18_053[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "b", lw=2, ms=7)

        d, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "r", lw=2, ms=7)
        d, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "k", lw=2, ms=7)
        d, _ = datalist_bin5different_gammas_test2_HQ10000_G1_0_18_053[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "b", lw=2, ms=7)

    if A:
        ax1.set_title(
            r"Time evolution of files = %s, $R_{middle} = 19.95$" % A_HQ0[:-9],
            fontsize=20,
        )

        Plt(1, datalist_bin5different_gammas_A_HQ10000_G1_0_0_000[0], "r")
        Plt(1, datalist_bin5different_gammas_A_HQ10000_G1_0_10_005[0], "k")
        Plt(1, datalist_bin5different_gammas_A_HQ10000_G1_0_48_093[0], "b")

        Plt(2, datalist_bin5different_gammas_A_HQ10000_G1_0_0_000[4], "r", A_HQ0[11:])
        Plt(2, datalist_bin5different_gammas_A_HQ10000_G1_0_10_005[4], "k", A_HQ66[11:])
        Plt(
            2, datalist_bin5different_gammas_A_HQ10000_G1_0_48_093[4], "b", A_HQ382[11:]
        )

        Plt(3, datalist_bin5different_gammas_A_HQ10000_G1_0_0_000[0], "r")
        Plt(3, datalist_bin5different_gammas_A_HQ10000_G1_0_10_005[0], "k")
        Plt(3, datalist_bin5different_gammas_A_HQ10000_G1_0_48_093[0], "b")

        Plt(4, datalist_bin5different_gammas_A_HQ10000_G1_0_0_000[4], "r")
        Plt(4, datalist_bin5different_gammas_A_HQ10000_G1_0_10_005[4], "k")
        Plt(4, datalist_bin5different_gammas_A_HQ10000_G1_0_48_093[4], "b")

        d, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_0_000[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "r", lw=2, ms=7)
        d, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_10_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "k", lw=2, ms=7)
        d, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_48_093[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "b", lw=2, ms=7)

        d, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_0_000[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "r", lw=2, ms=7)
        d, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_10_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "k", lw=2, ms=7)
        d, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_48_093[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "b", lw=2, ms=7)

        d, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_0_000[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "r", lw=2, ms=7)
        d, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_10_005[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "k", lw=2, ms=7)
        d, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_48_093[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "b", lw=2, ms=7)

        d, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_0_000[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "r", lw=2, ms=7)
        d, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_10_005[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "k", lw=2, ms=7)
        d, _ = datalist_bin5different_gammas_A_HQ10000_G1_0_48_093[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "b", lw=2, ms=7)

    if B:
        ax1.set_title(
            r"Time evolution of files = %s, $R_{middle} = 19.95$" % B_HQ0[:-9],
            fontsize=20,
        )

        Plt(1, datalist_bin5different_gammas_B_HQ10000_G1_0_0_000[0], "r")
        Plt(2, datalist_bin5different_gammas_B_HQ10000_G1_0_0_000[4], "r", B_HQ0[11:])
        Plt(3, datalist_bin5different_gammas_B_HQ10000_G1_0_0_000[0], "r")
        Plt(4, datalist_bin5different_gammas_B_HQ10000_G1_0_0_000[4], "r")
        d, _ = datalist_bin5different_gammas_B_HQ10000_G1_0_0_000[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "r", lw=2, ms=7)
        d, _ = datalist_bin5different_gammas_B_HQ10000_G1_0_0_000[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "r", lw=2, ms=7)
        d, _ = datalist_bin5different_gammas_B_HQ10000_G1_0_0_000[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "r", lw=2, ms=7)
        d, _ = datalist_bin5different_gammas_B_HQ10000_G1_0_0_000[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "r", lw=2, ms=7)

if Fig6b_GPerts_R_middle_31_62_vt_divided_by_gauss_and_Tsallis:
    f, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(4, 2)

    if test:
        for i in range(1, 7):
            exec(f"ax{i}.grid()")

        for i in range(1, 7):
            exec(f"ax{i}.set_xticklabels([])")

        for i in range(1, 7):
            exec(
                f"legend(prop=dict(size=13), numpoints=2, ncol=1,\
                          frameon=True, loc=0, handlelength=2.5)"
            )

        ax1.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)
        ax1.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        ax1.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        ax1.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        ax1.plot(data[:, 0], data[:, 1], "m", lw=2, ms=7)
        ax1.set_ylabel(r"$f\left(u \right)$", fontsize=20)
        ax1.set_title(
            r"Time evolution of files = %s, different r bins,\
                      $\gamma = -2.0$"
            % HQ0[:-9],
            fontsize=20,
        )

        ax2.plot(data[:, 0], data[:, 1], "r", HQ12[9:], lw=2, ms=7)
        ax2.plot(data[:, 0], data[:, 1], "g", HQ24[9:], lw=2, ms=7)
        ax2.plot(data[:, 0], data[:, 1], "k", HQ36[9:], lw=2, ms=7)
        ax2.plot(data[:, 0], data[:, 1], "b", HQ48[9:], lw=2, ms=7)
        ax2.plot(data[:, 0], data[:, 1], "m", HQ60[9:], lw=2, ms=7)
        ax2.set_ylabel(r"$f\left(\log \left(|u_n|,u_p \right)\right)$", fontsize=20)

        ax3.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        ax3.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        ax3.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        ax3.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)
        ax3.plot(data[:, 0], data[:, 1], "m", lw=2, ms=7)
        ax3.set_ylabel(r"$\log \left(f\left(u \right)\right)$", fontsize=20)
        ax3.set_yscale("log")

        ax4.plot(data[:, 0], data[:, 1], "r", lw=2, ms=7)
        ax4.plot(data[:, 0], data[:, 1], "g", lw=2, ms=7)
        ax4.plot(data[:, 0], data[:, 1], "k", lw=2, ms=7)
        ax4.plot(data[:, 0], data[:, 1], "b", lw=2, ms=7)
        ax4.plot(data[:, 0], data[:, 1], "m", lw=2, ms=7)
        ax4.set_ylabel(
            r"$\log \left(f\left(\log \left(|u_n|,u_p \right)\
                       \right) \right)$",
            fontsize=20,
        )
        ax4.set_yscale("log")

        def denom_ax5(a):
            return np.log10(a) * np.exp(-0.5 * a**2)

        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "r", lw=2, ms=7)
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "g", lw=2, ms=7)
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "k", lw=2, ms=7)
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "b", lw=2, ms=7)
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "m", lw=2, ms=7)
        ax5.set_ylabel(r"$\frac{f\left(u \right)}{log(x)e^{-0.5x^2}}$", fontsize=20)

        def denom_ax6(a):
            return np.exp(-0.5 * a**2)

        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "r", lw=2, ms=7)
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "g", lw=2, ms=7)
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "k", lw=2, ms=7)
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "b", lw=2, ms=7)
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "m", lw=2, ms=7)
        ax6.set_ylabel(
            r"$\frac{f\left(\log\left(|u_n|,u_p\right)\right)}\
                       {e^{-0.5x^2}}$",
            fontsize=20,
        )

    else:
        for i in range(1, 9):
            exec(f"ax{i}.grid()")

        for i in range(1, 3):
            exec(
                f"legend(prop=dict(size=13), numpoints=2, ncol=1,\
                          frameon=True, loc=0, handlelength=2.5)"
            )

        ax1.set_ylabel(r"$f\left(u_t\right)$", fontsize=20)
        ax2.set_ylabel(r"$f\left(\log \left( |u_tn|,u_tp \right)\right)$", fontsize=20)
        ax3.set_ylabel(r"$\log\left(f\left(u_t\right)\right)$", fontsize=20)
        ax3.set_yscale("log")
        ax4.set_ylabel(
            r"$\log \left( f\left(\log \left(|u_tn|, u_tp\
                       \right)\right) \right)$",
            fontsize=20,
        )
        ax4.set_yscale("log")
        ax5.set_ylabel(
            r"$\frac{f\left( u_t \right)}{887.569 \cdot x\
                       \cdot e^{-0.922 \cdot x^2}}$",
            fontsize=20,
        )
        ax6.set_ylim(0, 5)
        ax6.set_ylabel(
            r"$\frac{f\left(\log \left( |u_tn|,u_tp \right)\right)}\
                       {3424.993 \cdot x^2 \cdot e^{-0.930 \cdot x^2 }}$",
            fontsize=20,
        )
        ax7.set_ylim(0, 2)
        ax7.set_xlabel(r"$u_t$", fontsize=20)
        ax7.set_ylabel(r"$\frac{f\left(u_t\right)}{Tsallis}$", fontsize=20)
        ax8.set_ylim(0, 5)
        ax8.set_xlabel(r"$\log \left( |u_tn|,u_tp \right)$", fontsize=20)
        ax8.set_ylabel(
            r"$\frac{f\left(\log \left( |u_tn|, u_tp \right)\
                       \right)}{Tsallis}$",
            fontsize=20,
        )

    if test2:
        Plt(1, datalist_bin6different_gammas_test2_HQ10000_G1_0_0_000[0], "r")
        Plt(1, datalist_bin6different_gammas_test2_HQ10000_G1_0_10_005[0], "k")
        Plt(1, datalist_bin6different_gammas_test2_HQ10000_G1_0_18_053[0], "b")
        ax1.set_title(
            r"Time evolution of files = %s, $ R_{middle} = 31.62$" % test2_HQ0[:-9],
            fontsize=20,
        )

        Plt(
            2,
            datalist_bin6different_gammas_test2_HQ10000_G1_0_0_000[4],
            "r",
            test2_HQ0[9:],
        )
        Plt(
            2,
            datalist_bin6different_gammas_test2_HQ10000_G1_0_10_005[4],
            "k",
            test2_HQ66[9:],
        )
        Plt(
            2,
            datalist_bin6different_gammas_test2_HQ10000_G1_0_18_053[4],
            "b",
            test2_HQ166[9:],
        )

        Plt(3, datalist_bin6different_gammas_test2_HQ10000_G1_0_0_000[0], "r")
        Plt(3, datalist_bin6different_gammas_test2_HQ10000_G1_0_10_005[0], "k")
        Plt(3, datalist_bin6different_gammas_test2_HQ10000_G1_0_18_053[0], "b")

        Plt(4, datalist_bin6different_gammas_test2_HQ10000_G1_0_0_000[4], "r")
        Plt(4, datalist_bin6different_gammas_test2_HQ10000_G1_0_10_005[4], "k")
        Plt(4, datalist_bin6different_gammas_test2_HQ10000_G1_0_18_053[4], "b")

        d, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "r", lw=2, ms=7)
        d, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "k", lw=2, ms=7)
        d, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_18_053[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "b", lw=2, ms=7)

        d, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "r", lw=2, ms=7)
        d, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "k", lw=2, ms=7)
        d, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_18_053[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "b", lw=2, ms=7)

        d, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_0_000[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "r", lw=2, ms=7)
        d, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_10_005[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "k", lw=2, ms=7)
        d, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_18_053[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "b", lw=2, ms=7)

        d, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_0_000[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "r", lw=2, ms=7)
        d, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_10_005[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "k", lw=2, ms=7)
        d, _ = datalist_bin6different_gammas_test2_HQ10000_G1_0_18_053[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "b", lw=2, ms=7)

    if A:
        Plt(1, datalist_bin6different_gammas_A_HQ10000_G1_0_0_000[0], "r")
        Plt(1, datalist_bin6different_gammas_A_HQ10000_G1_0_10_005[0], "k")
        Plt(1, datalist_bin6different_gammas_A_HQ10000_G1_0_48_093[0], "b")
        ax1.set_title(
            r"Time evolution of files = %s, $R_{middle} = 31.62$" % A_HQ0[:-9],
            fontsize=20,
        )

        Plt(2, datalist_bin6different_gammas_A_HQ10000_G1_0_0_000[4], "r", A_HQ0[11:])
        Plt(2, datalist_bin6different_gammas_A_HQ10000_G1_0_10_005[4], "k", A_HQ66[11:])
        Plt(
            2, datalist_bin6different_gammas_A_HQ10000_G1_0_48_093[4], "b", A_HQ382[11:]
        )

        Plt(3, datalist_bin6different_gammas_A_HQ10000_G1_0_0_000[0], "r")
        Plt(3, datalist_bin6different_gammas_A_HQ10000_G1_0_10_005[0], "k")
        Plt(3, datalist_bin6different_gammas_A_HQ10000_G1_0_48_093[0], "b")

        Plt(4, datalist_bin6different_gammas_A_HQ10000_G1_0_0_000[4], "r")
        Plt(4, datalist_bin6different_gammas_A_HQ10000_G1_0_10_005[4], "k")
        Plt(4, datalist_bin6different_gammas_A_HQ10000_G1_0_48_093[4], "b")

        d, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_0_000[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "r", lw=2, ms=7)
        d, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_10_005[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "k", lw=2, ms=7)
        d, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_48_093[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "b", lw=2, ms=7)

        d, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_0_000[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "r", lw=2, ms=7)
        d, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_10_005[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "k", lw=2, ms=7)
        d, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_48_093[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "b", lw=2, ms=7)

        d, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_0_000[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "r", lw=2, ms=7)
        d, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_10_005[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "k", lw=2, ms=7)
        d, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_48_093[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "b", lw=2, ms=7)

        d, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_0_000[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "r", lw=2, ms=7)
        d, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_10_005[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "k", lw=2, ms=7)
        d, _ = datalist_bin6different_gammas_A_HQ10000_G1_0_48_093[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "b", lw=2, ms=7)

    if B:
        Plt(1, datalist_bin6different_gammas_B_HQ10000_G1_0_0_000[0], "r")
        ax1.set_title(
            r"Time evolution of files = %s, $R_{middle} = 31.62$" % B_HQ0[:-9],
            fontsize=20,
        )

        Plt(2, datalist_bin6different_gammas_B_HQ10000_G1_0_0_000[4], "r", B_HQ0[11:])
        Plt(3, datalist_bin6different_gammas_B_HQ10000_G1_0_0_000[0], "r")
        Plt(4, datalist_bin6different_gammas_B_HQ10000_G1_0_0_000[4], "r")
        d, _ = datalist_largeRmiddle_31_62_differentGammas_B_HQ10000_G1_0_0_000[0]
        ax5.plot(d[:, 0], d[:, 1] / denom_ax5(d[:, 0]), "r", lw=2, ms=7)
        d, _ = datalist_bin6different_gammas_B_HQ10000_G1_0_0_000[4]
        ax6.plot(d[:, 0], d[:, 1] / denom_ax6(d[:, 0]), "r", lw=2, ms=7)
        d, _ = datalist_bin6different_gammas_B_HQ10000_G1_0_0_000[0]
        ax7.plot(d[:, 0], d[:, 1] / denom_ax7(d[:, 0]), "r", lw=2, ms=7)
        d, _ = datalist_bin6different_gammas_B_HQ10000_G1_0_0_000[4]
        ax8.plot(d[:, 0], d[:, 1] / denom_ax8(d[:, 0]), "r", lw=2, ms=7)

plt.show()
