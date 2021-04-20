import subprocess
import os
import multiprocessing.dummy

def GetTicks(statsfile):
    with open(statsfile, 'r') as f:
        for line in f:
            if 'sim_ticks' in line:
                return int(line.split()[1])
spec_home_directory = "/p/prometheus/private/adarsh1/spec2006_apps"
benchmark_directories = {
    'milc':'433.milc',
    'soplex':'450.soplex',
    'sphinx3':'482.sphinx3',
    'povray':'453.povray',
    'zeusmp':'434.zeusmp',
    'GemsFDTD':'459.GemsFDTD',
    'lbm':'470.lbm',
    'bwaves':'410.bwaves',
    'namd':'444.namd',
    'calculix':'454.calculix',
    'leslie3d':'437.leslie3d',
    'gromacs':'435.gromacs',
    'bzip2':'401.bzip2',
    'mcf':'429.mcf',
    'hmmer':'456.hmmer',
    'libquantum':'462.libquantum',
    'h264ref':'464.h264ref',
    'omnetpp':'471.omnetpp',
    'astar':'473.astar',
    'sjeng':'458.sjeng',
    'gobmk':'445.gobmk'}

#//benchmarks = ['401.bzip2','403.gcc','410.bwaves','416.gamess','429.mcf',
#//                  '433.milc','434.zeusmp','435.gromacs','436.cactusADM',
#//                  '437.leslie3d','444.namd','445.gobmk','453.povray',
#//                  '454.calculix','456.hmmer','458.sjeng','459.GemsFDTD',
#//                  '462.libquantum','464.h264ref','465.tonto','470.lbm',
#//                  '471.omnetpp','473.astar','481.wrf','482.sphinx3',
#//                  '998.specrand','999.specrand']

def RunAndGetTicks(cliargs, benchmark, outdir, pipe_to_file=True):
    if pipe_to_file:
        proc = subprocess.Popen(cliargs,
                stdout=open(spec_home_directory + \
            '/'+benchmark + \
            '/run/run_base_ref_i386-m32-gcc42-nn.0000/'+ \
            outdir + '/stdout.txt', 'w+'),
                stderr=open(spec_home_directory + \
                        '/'+benchmark + \
                        '/run/run_base_ref_i386-m32-gcc42-nn.0000/'\
                        + outdir + '/stderr.txt', 'w+'))
    else:
        proc = subprocess.Popen(cliargs)
    proc.wait()
    print("Benchmark {} finished\n".format(benchmark))
   # return GetTicks('{}/stats.txt'.format(spec_home_directory + \
   #     benchmark_directories[benchmark]+\
   #            '/run/run_base_ref_i386-m32-gcc42-nn.0000/'+ outdir))

curWorkingDirectory = os.getcwd()


def RunBenchmark(benchmark_name):
    runtype = '_PJ_'
    checkpoint_dir = '_VC_DSR_O3CPU_squashed_load_analysis'
#    runtype = '_pointer_chased_loads_ref'
    print(benchmark_name)
    target_path = spec_home_directory + \
            '/'+benchmark_name + \
            '/run/run_base_ref_i386-m32-gcc42-nn.0000/'+\
            benchmark_name+runtype
    print(target_path)
    if not(os.path.isdir(target_path)):
        os.makedirs(target_path)
    target_path = curWorkingDirectory + "/"+  benchmark_name+runtype
    #print(target_path)
    if not(os.path.isdir(target_path)):
        os.makedirs(target_path)
    cliargs = [
            'run_gem5_x86_spec06_benchmark.sh',
            '{}'.format(benchmark_name),
            '{}'.format(benchmark_name+runtype),
            '{}'.format(benchmark_name + checkpoint_dir)
            ]
    proc = subprocess.Popen(cliargs)
    proc.wait()
    return RunAndGetTicks(cliargs,benchmark_name,benchmark_name+runtype)

#benchmark_names = ['milc','soplex','sphinx3','povray',
#        'zeusmp','GemsFDTD','lbm','bwaves','namd','calculix',
#        'leslie3d','gromacs','bzip2','mcf','hmmer','libquantum',
#        'h264ref','omnetpp','astar','sjeng','gobmk']
#benchmark_names = ['namd','astar','gromacs']
#benchmark_names = ['lbm','povray','bwaves','h264ref']
#benchmark_names = ['bzip2','GemsFDTD','leslie3d','milc','soplex','zeusmp','gromacs','namd','lbm','sjeng','astar','bwaves','h264ref','libquantum']
#benchmark_names = ['bzip2','bwaves','mcf','milc','zeusmp','gromacs','leslie3d','namd','gobmk','calculix','hmmer','GemsFDTD','libquantum','h264ref','lbm','omnetpp','astar','sphinx_livepretend']
#benchmark_names = ['bzip2','bwaves','mcf','milc','zeusmp','gromacs','leslie3d','namd','gobmk','calculix','hmmer','GemsFDTD','libquantum','h264ref','lbm','omnetpp','astar']
#benchmark_names = ['bwaves','mcf','milc','zeusmp','gromacs','leslie3d','namd','gobmk','calculix','hmmer','GemsFDTD','libquantum','lbm','omnetpp','astar']
#benchmark_names = ['bzip2','bwaves','mcf','milc','zeusmp','gromacs','leslie3d','namd','calculix','hmmer','GemsFDTD','libquantum','h264ref','lbm','omnetpp','astar']
#benchmark_names = ['h264ref','bzip2','gromacs','omnetpp']
#benchmark_names = ['lbm']
#benchmark_names = ['cactusADM']
#benchmark_names = ['bzip2','bwaves','mcf','milc','zeusmp','gromacs','leslie3d','namd','calculix','hmmer','GemsFDTD','libquantum','h264ref','lbm','omnetpp','astar','soplex','sjeng','gobmk']
#benchmark_names = ['astar','bzip2','bwaves','calculix','GemsFDTD','gobmk','gromacs','h264ref','hmmer','lbm','leslie3d','libquantum','mcf','milc','namd','omnetpp','povray','zeusmp','soplex','sjeng','sphinx']

#benchmark_names = ['bzip2','bwaves','mcf','milc','zeusmp','gromacs','leslie3d','namd','calculix','hmmer','GemsFDTD','libquantum','h264ref','lbm','omnetpp','astar','soplex','sjeng','gobmk','povray','specrand','tonto','sphinx','wrf','cactusADM']
#benchmark_names = ['perlbench', 'gcc', 'xalancbmk', 'gamess', 'cactusADM', 'dealII', 'tonto', 'wrf', 'sphinx3']
benchmark_names = ['astar']
p = multiprocessing.dummy.Pool(len(benchmark_names))
tick_counts = p.map(RunBenchmark,benchmark_names)
#print(tick_counts)
