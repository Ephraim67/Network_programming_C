import paramiko

hostname = "193.83.255.255:2028"
port = 2028
username = "root"
private_key_path = "private_key.pem"
# cert_path = ""

#Swift transaction ID to check
swift_transaction_id = ""

#initialize SHH client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

private_key = paramiko.RSAKey(filename=private_key_path, password="test")

try:
    #let's connect to swfit server
    ssh.connect(
        hostname=hostname,
        port=port,
        username=username,
        pkey=private_key
    )

    print("Conected to the server successfully.")

    command = f"check_swift_id --id {swift_transaction_id}"

    stdin, stdout, stderr = ssh.exec_command(command)
    output = stdout.read().decode('utf-8')
    error = stderr.read().decode('utf-8')

    # Process the response from the server
    if output:
        print("Server Response", output)
    if error:
        print("Eror", error)

except Exception as e:
    print(f"An error occured: {e}")

finally:
    # close connection
    ssh.close()