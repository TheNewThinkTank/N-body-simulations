import matplotlib.pyplot as plt  # type: ignore
import pylab  # type: ignore
import file_lists.file_lists as lsts  # type: ignore

datalistMartinIC = [(pylab.loadtxt(f), l) for f, l in lsts.fileLstMartinIC]
datalistMartinFinal = [(pylab.loadtxt(f), l) for f, l in lsts.fileLstMartinFinal]

datalistA = [(pylab.loadtxt(f), l) for f, l in lsts.fileLstA]
datalistA_R10000 = [(pylab.loadtxt(f), l) for f, l in lsts.fileLstA_R10000]
datalist_A_R10000_20bins = [
    (pylab.loadtxt(f), l) for f, l in lsts.FileLstA_R10000_20bins
]

colors = ["Green", "Red", "Black"]
HQ12 = ""

# fls.Bin1differentGammasTest2HQ10000_G1_0_0_000 = [(pylab.loadtxt(f), l)
#                                              for f, l in bins3A[0]]


def plot_test():
    # return fls.Bin1differentGammasTest2HQ10000_G1_0_0_000
    # f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2,
    #                                            sharex='col', sharey='row')

    # data, label = fls.Bin1differentGammasTest2HQ10000_G1_0_0_000[0]
    # ax1.plot(data[:, 0], data[:, 1],\
    #                  color={colours[fileNum]}, ls='--', lw=2, ms=7)")
    pass


# plot_test()


def plot_binData(fileLst):
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex="col", sharey="row")
    for axNum in range(1, 5):
        for binNum in range(1, 5):
            for fileNum in range(1, 4):
                exec(f"data, label = lsts.Bin{binNum}{fileLst}[{fileNum}]")
                exec(
                    f"ax{axNum}.plot(data[:, 0], data[:, 1],\
                     color={colors[fileNum - 1]}, ls='--', lw=2, ms=7)"
                )
        exec(f"ax1{axNum}.grid()")

    ax1.set_ylabel(r"$f\left(u \right)$", fontsize=20)
    ax1.set_title(r"File = %s" % HQ12, fontsize=20)

    ax2.set_ylabel(r"$f\left(\log\left(|u_n|, u_p \right)\right)$", fontsize=20)

    ax1_labels = [r"$v_r$", r"$v_{\theta}$", r"$v_{\phi}$"]
    ax2_labels = [
        r"$\gamma = -1.5$",
        r"$\gamma = -2.0$",
        r"$\gamma = -2.5$",
        r"$\gamma = -3.0 $",
    ]

    for i in range(len(ax1_labels)):
        ax1.plot([], [], label=ax1_labels[i], ls="--", lw=2, ms=7)

    for i in range(len(ax2_labels)):
        ax2.plot([], [], label=ax2_labels[i], ls="--", lw=2, ms=7)

    for binNum in range(1, 3):
        exec(
            f"ax{binNum}.legend(prop=dict(size=13), numpoints=2, ncol=1,\
             frameon=True, loc=0, handlelength=2.5"
        )

    ax3.set_xlabel(r"$u_r$, $u_{\theta}$ and $u_{\phi}$", fontsize=20)
    ax3.set_ylabel(r"$\log \left( f(u) \right)$", fontsize=20)

    ax4.set_xlabel(
        r"$\log \left( |u_rn|,u_rp \right)$, $\log\
                   \left( |u_{\theta}n|,u_{\theta}p \right)$ and\
                   $\log \left( |u_{\phi}n|,u_{\phi}p \right)$",
        fontsize=20,
    )
    ax4.set_ylabel(
        r"$\log \left( f\left(\log \left( |u_n|,\
                   u_p \right)\right) \right)$",
        fontsize=20,
    )

    ax3.set_yscale("log")
    ax4.set_yscale("log")


plot_binData("HQ10000_G1_2_1_005")
# plot_binData('different_gammas_test2_HQ10000_G1_0_0_000')
