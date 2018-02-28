import numpy as np
from numpy import linalg as la


"""
D-algorithm 矩阵信息压缩，菜谱推荐（传统机器学习算法）
数据格式: [[菜 品：菜品A, 菜品，菜品C]
          [用户A：1，    0，     2]
          [用户B：2，    1，     0]]
"""


def euclidSim(inA, inB):
    """
    欧式距离
    :param inA:
    :param inB:
    :return:
    """
    return 1.0 / (1.0 + la.norm(inA - inB))


def pearsSim(inA, inB):
    """
    皮尔逊相似度
    :param inA:
    :param inB:
    :return:
    """
    if len(inA) < 3:
        return 1.0
    return 0.5 + 0.5 * np.corrcoef(inA, inB, rowvar=0)[0][1]


def cosSim(inA, inB):
    """
    余弦相似度
    :param inA:
    :param inB:
    :return:
    """
    num = np.float(inA.T * inB)
    denom = la.norm(inA) * la.norm(inB)
    return 0.5 + 0.5 * (num / denom)


def standEst(dataMat, user, simMeas, item):
    """

    :param dataMat:
    :param user:
    :param simMeas:
    :param item:
    :return:
    """
    n = np.shape(dataMat)[1]
    u, sigma, vt = la.svd(dataMat)

    def cul_min_dataMat(sigma):
        """
        矩阵压缩信息控制
        :param sigma:
        :return:
        """
        sigma_2 = sigma ** 2
        sigma_sum = np.sum(sigma_2) * 0.9
        for i in range(len(1, sigma_2)):
            if np.sum(sigma_2[: i]) >= sigma_sum:
                return np.mat(np.eye(i + 1) * sigma[: i + 1])
        return dataMat

    dataMat = cul_min_dataMat(sigma)
    simTotal = 0.0; ratSimTotal = 0.0
    for j in range(n):
        userRating = dataMat[user, j]
        if userRating == 0:
            continue
        overLap = np.nonzero(np.logical_and(dataMat[:, item].A > 0, dataMat[:, j].A > 0))[0]
        if len(overLap) == 0:
            similarity = 0
        else:
            similarity = simMeas(dataMat[overLap, item], dataMat[overLap, j])
        simTotal += similarity
        ratSimTotal += similarity * userRating
    if simTotal == 0:
        return 0
    return ratSimTotal / simTotal


def recommend(dataMat, user, N=3, simMeans=cosSim, estMethod=standEst):
    """
    推荐结果
    :param dataMat:
    :param user:
    :param N:
    :param simMeans:
    :param estMethod:
    :return:
    """
    unrateItems = np.nonzero(dataMat[user, :].A == 0)[1]
    if len(unrateItems) == 0:
        return
    itemScores = []
    for item in unrateItems:
        estimatedScore = estMethod(dataMat, user, simMeans, item)
        itemScores.append(item, estimatedScore)
    return sorted(itemScores, key=lambda jj: jj[1], reverse=True)[: N]


def svdEst(dataMat, user, simMeas, item, compression_ratio):
    n = np.shape(dataMat)[1]
    simTotal = 0.0; ratSimTotal = 0.0
    U, Sigma, VT = la.svd(dataMat)
    Sig = np.mat(np.eye(compression_ratio) * Sigma[: compression_ratio])
    xformedItems = dataMat.T * U[:, : compression_ratio] * Sig.I
    for j in range(n):
        userRating = dataMat[user, j]
        if userRating == 0 or j == item: continue
        similarity = simMeas(xformedItems[item, :].T, xformedItems[j, :].T)
        print 'the %d and %d similarity is : %f' % (item, j, similarity)
        simTotal += similarity
        ratSimTotal += similarity * userRating
        if simTotal == 0: return 0
        else: return ratSimTotal / simTotal


def load_data_from_db():
    pass
