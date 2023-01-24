FROM rust:1.66

WORKDIR /opt
COPY Cargo.lock Cargo.toml /opt/
COPY src/main.rs /opt/src/

#CMD run --package rust --bin rust
CMD cargo run --package rust --bin rust --release