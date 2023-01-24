use std::process::exit;
use std::time::{Duration, Instant};

const SUM_EVEN_NUMBERS_CODE: &str = "
fn sum_even_numbers(bottom: i64, top: i64) -> i64 {
    return (bottom..=top).filter(|x| x % 2 == 0).sum()
}
";

fn sum_even_numbers(bottom: i64, top: i64) -> i64 {
    return (bottom..=top).filter(|x| x % 2 == 0).sum()
}

fn main() {
    let repeats = 100;
    let mut min_execution_time = Duration::MAX;

    for _ in 0..repeats {
        let start_at = Instant::now();
        let res = sum_even_numbers(2, 20_000_000);

        let execution_time =  start_at.elapsed();
        if execution_time < min_execution_time {
            min_execution_time = execution_time;
        }

        // disable optimization
        if res == 0 {
            exit(res as i32)
        }
    }

    println!("Test case: sum_even_numbers(2, 20_000_000)  ");
    println!();
    println!("```rust");
    println!("{}", SUM_EVEN_NUMBERS_CODE.strip_prefix("\n").unwrap().strip_suffix("\n").unwrap());
    println!("```");
    println!("Repeats: {}  ", repeats);
    println!("Best execution time: {:.2?}  ", min_execution_time);
}
