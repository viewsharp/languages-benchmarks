use std::time::Instant;


fn sum_even_numbers(bottom: i64, top: i64) -> i64 {
    return (bottom..=top).filter(|x| x % 2 == 0).sum()
}

fn main() {
    let start_at = Instant::now();
    let res = sum_even_numbers(2, 20_000_000);
    println!("{:.2?}", start_at.elapsed());
    println!("{}", res)
}
