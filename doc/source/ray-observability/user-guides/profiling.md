(profiling)=
# Profiling
Profiling is one of the most important debugging tools to diagnose performance, out of memory, hanging, or other application issues.
Here is a list of common profiling tools you may use when debugging Ray applications. 
- CPU profiling
    - py-spy
- Memory profiling
    - memray
- GPU profiling
    - PyTorch Profiler
- Ray Task / Actor timeline

If Ray doesn't work with certain profiling tools, try running them without Ray to debug the issues.

(profiling-cpu)=
## CPU profiling
Profile the CPU usage for Driver and Worker processes. This helps you understand the CPU usage by different processes and debug unexpectedly high or low usage.

(profiling-pyspy)=
### py-spy
[py-spy](https://github.com/benfred/py-spy/tree/master) is a sampling profiler for Python programs. Ray Dashboard has native integration with pyspy:

- It lets you visualize what your Python program is spending time on without restarting the program or modifying the code in any way.
- It dumps the stacktrace of the running process so that you can see what the process is doing at a certain time. It is useful when programs hangs.

:::{note}
You may run into permission errors when using py-spy in the docker containers. To fix the issue:

- if you start Ray manually in a Docker container, follow the `py-spy documentation`_ to resolve it. 
- if you are a KubeRay user, follow the :ref:`guide to configure KubeRay <kuberay-pyspy-integration>` and resolve it.
:::

Here are the {ref}`steps to use py-spy with Ray and Ray Dashboard <observability-debug-hangs>`.

(profiling-cprofile)=
### cProfile
cProfile is Python’s native profiling module to profile the performance of your Ray application.

Here are the {ref}`steps to use cProfile <dashboard-cprofile>`.

(profiling-memory)=
## Memory profiling
Profile the memory usage for Driver and Worker processes. This helps you analyze memory allocations in applications, trace memory leaks, and debug high/low memory or out of memory issues.

(profiling-memray)=
### memray
memray is a memory profiler for Python. It can track memory allocations in Python code, in native extension modules, and in the Python interpreter itself.

Here are the {ref}`steps to profile the memory usage of Ray Tasks and Actors <memray-profiling>`.

(profiling-gpu)=
## GPU profiling
GPU and GRAM profiling for your GPU workloads like distributed training. This helps you analyze performance and debug memory issues. 
- PyTorch profiler is supported out of box when used with Ray Train
- NVIDIA Nsight System is not natively supported yet. Leave your comments in this [feature request for Nisght System support](https://github.com/ray-project/ray/issues/19631).

(profiling-pytoch-profiler)=
### PyTorch Profiler
PyTorch Profiler is a tool that allows the collection of performance metrics (especially GPU metrics) during training and inference.

Here are the {ref}`steps to use PyTorch Profiler with Ray Train or Ray Data <performance-debugging-gpu-profiling>`.

(profiling-timeline)=
## Ray Task / Actor timeline
Ray Timeline profiles the execution time of Ray Tasks and Actors. This helps you analyze performance, identify the stragglers, and understand the distribution of workloads.

Open your Ray Job in Ray Dashboard and follow the {ref}`instructions to download and visualize the trace files <dashboard-timeline>` generated by Ray Timeline.
