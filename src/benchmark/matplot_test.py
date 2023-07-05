# Importing libraries
import matplotlib.pyplot as plt
import numpy as np
from statistics import median, mean
from unco import UNCO_PATH
from pathlib import Path

def _plot_results_increasing_alternatives(X : range, results : list[list[list[float]]], querylist : list[int], modellist : list[int], increasing_alternatives : bool):
    output = [[[] for _ in modellist] for _ in querylist]
    for res in results:
        for query_numb, query_res in enumerate(res):
            for model_numb, model_res in enumerate(query_res):
                output[query_numb][model_numb].append(model_res)
    
    for index, query_numb in enumerate(querylist):
        fig = plt.figure()
        for modelindex, model_numb in enumerate(modellist):
            color, linestyle = "r", "-"
            if model_numb == 9: model_numb = "9a"
            model_numb = "9b" if model_numb == 10 else str(model_numb)
            plt.plot(X, output[index][modelindex], color=color, linestyle=linestyle, label=str(model_numb))

        if increasing_alternatives: plt.xlabel("#Alternatives per uncertain statement")
        else: plt.xlabel("#Uncertainties per column")

        plt.ylabel("Time in seconds")
        if increasing_alternatives: plt.title(f"Query {query_numb} with increasing numb alternatives")
        else: plt.title(f"Query {query_numb} with increasing numb uncertainties")

        plt.legend()

        plt.ylim([0.3, 0.45])

        if increasing_alternatives: plt.savefig(Path(UNCO_PATH,f"src/benchmark/results/alternatives{query_numb}.pdf"), format="pdf", bbox_inches="tight")
        else: plt.savefig(Path(UNCO_PATH,f"src/benchmark/results/uncertainties{query_numb}.pdf"), format="pdf", bbox_inches="tight")

        plt.close(fig)
            # plt.show()
# Using Numpy to create an array X

  
# raw2
res = [[[0.31581735610961914, 0.316461443901062, 0.2972449064254761, 0.30834710597991943, 0.31610798835754395]], [[0.31742382049560547, 0.32586634159088135, 0.3242994546890259, 0.3321026563644409, 0.323238730430603]], [[0.3202708959579468, 0.3297187089920044, 0.3758777379989624, 0.3132728338241577, 0.3390456438064575]], [[0.32495248317718506, 0.34338557720184326, 0.3421649932861328, 0.382671594619751, 0.3440277576446533]], [[0.3710055351257324, 0.34922969341278076, 0.3755371570587158, 0.31953907012939453, 0.34186267852783203]], [[0.3620065450668335, 0.3730134963989258, 0.37717926502227783, 0.3509582281112671, 0.3479503393173218]], [[0.35990142822265625, 0.3673804998397827, 0.348044753074646, 0.3825486898422241, 0.35394370555877686]], [[0.36579716205596924, 0.4142543077468872, 0.349450945854187, 0.3481963872909546, 0.37901735305786133]], [[0.3651919364929199, 0.36757636070251465, 0.4271751642227173, 0.355518102645874, 0.3768390417098999]], [[0.3596668243408203, 0.3457832336425781, 0.40120089054107666, 0.3930472135543823, 0.3863186836242676]], [[0.42096197605133057, 0.3691260814666748, 0.37250328063964844, 0.3891184329986572, 0.39053165912628174]]]

# median = 5
res = [[[0.30747389793395996, 0.3020329475402832, 0.30664944648742676, 0.3044455051422119, 0.29869019985198975]], [[0.3374934196472168, 0.31201863288879395, 0.3029102087020874, 0.3096134662628174, 0.3132673501968384]], [[0.3089708089828491, 0.31796371936798096, 0.32004761695861816, 0.3126600980758667, 0.3300468921661377]], [[0.3216143846511841, 0.3273056745529175, 0.31213390827178955, 0.316292405128479, 0.32383298873901367]], [[0.32285892963409424, 0.3319072723388672, 0.3198816776275635, 0.3166215419769287, 0.3121650218963623]], [[0.3314509391784668, 0.33919811248779297, 0.3290356397628784, 0.32667994499206543, 0.33666813373565674]], [[0.33795714378356934, 0.3285785913467407, 0.32093358039855957, 0.34092044830322266, 0.3270770311355591]], [[0.3585994243621826, 0.3474597930908203, 0.3388596773147583, 0.34146034717559814, 0.33688080310821533]], [[0.3464505672454834, 0.35600852966308594, 0.3388477563858032, 0.3399542570114136, 0.3470478057861328]], [[0.34879183769226074, 0.35839343070983887, 0.3562980890274048, 0.35866641998291016, 0.35130250453948975]], [[0.3641113042831421, 0.3581535816192627, 0.3588770627975464, 0.3523674011230469, 0.34496092796325684]]]

newres = [([median(l)] for l in sublist) for sublist in res]

print(_plot_results_increasing_alternatives(range(0,301,30),newres,querylist=[4],modellist=[1],increasing_alternatives=False))

# X = range(len(res[0][0]))[:10]

# results = res[0]

# plt.plot(X, results[0][:10], color='r', label='1')
# plt.plot(X, results[1][:10], color='b', label='2')
# plt.plot(X, results[2][:10], color='g', label='3')
# plt.plot(X, results[3][:10], color='y', label='4')
# plt.plot(X, results[4][:10], color='m', label='5')
# plt.plot(X, results[5][:10], color='c', label='6')
# plt.plot(X, results[6][:10], color='k', label='7')
# plt.plot(X, results[7][:10], color='y', label='8')

# plt.xlabel("#Uncertainties per column")
# plt.ylabel("Time")
# plt.title(f"Query {4} with increasing numb uncertainties")

# plt.legend()
# plt.show()

# print([l[:10] for l in results])
