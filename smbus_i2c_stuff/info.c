https://stackoverflow.com/questions/25982525/why-i2c-smbus-block-max-is-limited-to-32-bytes

Here's the documentation for the Linux i2c interface: https://www.kernel.org/doc/Documentation/i2c/dev-interface

At the simplest level you can use ioctl(I2C_SLAVE) to set the slave address and the write system call to write the command. Something like:

i2c_write(int file, int address, int subaddress, int size, char *data) {
    char buf[size + 1];               // note: variable length array
    ioctl(file, I2C_SLAVE, address);  // real code would need to check for an error
    buf[0] = subaddress;              // need to send everything in one call to write
    memcpy(buf + 1, data, size);      // so copy subaddress and data to a buffer 
    write(file, buf, size + 1); 
}
