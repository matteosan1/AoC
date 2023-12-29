use regex::Regex;

fn main() {
    let lines = vec![
"Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8",
"Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"
];


    let text = "This is a test string with the word 'test'";
    let pattern = r"test"; // This pattern matches the word "test"

    let regex = Regex::new(pattern).unwrap();
    let mut matches = regex.find_iter(&text);

    for match in matches {
        println!("Match: {:?}", match);
    }



    let mut names = Vec::<&str>::new();
    let mut ingredients = Vec::<Vec<i32>>::new();
    for (i, l) in lines.iter().enumerate() {
        let parts = l[0..l.len()-1].split_whitespace().collect::<Vec<&str>>();
        println!("{:?}", parts);
        let vals = parts[1..parts.len()].into_iter().map(|x| x.parse::<i32>().unwrap()).collect::<Vec<i32>>();
        names.push(parts[0]);
        ingredients.push(vals);
    }
    println!("{:?}", ingredients);
}