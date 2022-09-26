#!/bin/env python

import ROOT as r
import glob
import os
from os.path import exists


def getGenWeightSum(filename):
    f = r.TFile(filename)
    t = f.Get("Runs")
    genEventSumw = 0
    for i in t:
        genEventSumw += i.genEventSumw
    return genEventSumw

def parseYear(samplename):
    if "20UL18NanoAODv9" in samplename: return "2018"
    if "20UL17NanoAODv9" in samplename: return "2017"
    if "20UL16NanoAODv9" in samplename: return "2016"
    if "20UL16NanoAODAPVv9" in samplename: return "2016APV"

def parseLumi(samplename):
    if "20UL18NanoAODv9" in samplename: return 59.8
    if "20UL17NanoAODv9" in samplename: return 41.5
    if "20UL16NanoAODv9" in samplename: return 16.8
    if "20UL16NanoAODAPVv9" in samplename: return 19.5

if __name__ == "__main__":

    nanoskims = glob.glob("/ceph/cms/store/user/phchang/FourLepNanoSkim/v8/*")
    xsec_filename = "xsec.txt"
    xsecdb = dict([ [ x.split()[0][1:].replace("/","_")+"_v8", x.split()[1] ] for x in open(xsec_filename).readlines() ])

    for nanoskim in sorted(nanoskims):
        if "Run201" in nanoskim:
            continue
        output_file = nanoskim+"/merged/output.root"
        file_exists = exists(output_file)
        samplename = os.path.basename(nanoskim)
        genweight = getGenWeightSum(output_file)
        xsec = float(xsecdb[samplename])
        year = parseYear(samplename)
        lumi = parseLumi(samplename)
        print("{:300s},{:30.10f},{},{},{}".format(nanoskim, xsec * 1000 * lumi / genweight, year, lumi, genweight))
