open Support.Utils

let file = "day01/input.txt"

let parse_line (line : string) =
  String.split_on_char ' ' line |> List.map (fun _ -> 0)

let sum (lst : int list) = List.fold_left ( + ) 0 lst

let _compute (lines : string list) =
  List.map parse_line lines |> List.flatten |> sum

let () =
  let lines = read_lines file in
  _compute lines |> string_of_int |> print_endline
