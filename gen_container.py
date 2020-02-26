import argparse, os, subprocess

repo_base = "registry.columbustech.io/columbustech/"
project_name = "mapfn-foo"

parser = argparse.ArgumentParser(description="Generate Dockerfile for container")
parser.add_argument("-a", "--additional", help="Additional python files folder")
parser.add_argument("-f", "--profiler", help="Profiling function")
parser.add_argument("-r", "--requirements", help="Pip requirements file")
parser.add_argument("-n", "--name", help="Container name")
parser.add_argument("-u", "--user", help="Username")
parser.add_argument("-p", "--password", help="Password")
parser.add_argument("-b", "--base", help="Repository base path")
options = parser.parse_args()

base_path = os.path.join(os.path.join(options.name, "src"), "foo")

project_name = None
if options.name is not None:
    project_name = options.name
if options.base is not None:
    repo_base = options.base

subprocess.call(["git", "clone", "https://www.github.com/columbustech/mapfn-test"])
subprocess.call(["mv", "mapfn-test", options.name])
subprocess.call(["cp", options.profiler, os.path.join(base_path, "process.py")])

if options.additional is not None:
    subprocess.call(["cp", "-r", options.additional, base_path])

if options.requirements is not None:
    req = None
    with open(options.requirements, "r") as f:
        req = f.read()
    with open(os.path.join(options.name, "requirements.txt"), "a") as f:
        f.write(req)

subprocess.call(["docker", "build", "-t", project_name, "."], cwd=project_name)
subprocess.call(["docker", "login", "-u", options.user, "-p", options.password])
subprocess.call(["docker", "tag", project_name, repo_base + project_name])
subprocess.call(["docker", "push", repo_base + project_name])
