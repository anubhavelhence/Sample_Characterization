import time

time_array = []
time_array.append(time.strftime('%H:%M:%S'))

read_file = "unload_sample_exec"

log = open (read_file + "_" + time_array[0] + ".txt", "w")
log.close()

with open(read_file + ".txt", "r") as f:
    for line in f:
        print(line)
        input("")

        temp = time.strftime('%H:%M:%S')
        print (temp)

        time_array.append(time.strftime('%H:%M:%S'))

        with open (log.name, "a") as log:
            log.write(line + 'end:\t\t\t\t' + temp + '\n')

        log.close()
f.close()

