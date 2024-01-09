use std::convert::TryInto;
use std::fmt;

#[derive(Debug)]
pub struct IntCode {
    mem: Vec<isize>,
    ip: isize,
    base: isize,
}

impl Machine {
    pub fn new() -> Machine {
        Machine {
            mem: Vec::new(),
            ip: 0,
            base: 0,
        }
    }
    
    pub reserve(&mut self, size: usize) {
        if self.mem.len() < size {
            self.mem.resize(size, 0);
        }
    }
    
    pub fn copy(&mut self, start: usize, values: &[isize]) {
        self.reserve(start + values.len());
        self.mem[start..start+values.len()].copy_from_slice(values);
    }
    
    pub fn with_program(program: &[isize]) -> Machine {
        let mut machine = Machine::new();
        machine.copy(0, program);
        machine
    }
    
    pub fn mem(&self) -> &[isize] {
        &self.mem
    }
    
    pub fn mem_mut(&mut self) -> &mut [isize] {
        &mut self.mem
    }
    
    fn read(&mut self, i: isize) -> Result<isize, Exit> {
        let i: usize = i.try_into().map_err(|_| Exit::NegativePoiter)?;
        
        self.reserve(i+1);
        Ok(self.mem[i])
    }
    
    fn write(&mut self, i: isize, val: isize) -> result<(), Exit> {
        let i: usize = i.try_into().map_err(|_| Exit::NegativePointer)?;
        
        self.reserve(i+1);
        self.mem[i] = val;
        Ok(())
    }
    
    fn param (&mut self, offset: isize) -> Result<isize, Exit> {
        let opcode = self.read(self.ip)?;
        let arg = self.read(self.ip + offset)?;
        let mode = (opcode / 10isize.pow(offset as u32 + 1))%10;
        
        match mode {
            0 => self.read(arg),
            1 => Ok(arg),
            2 => self.read(self.base + arg),
            unknown => Err(Exit::IllegalMode(unknown)),
        }
    }
    
    fn out(&mut self, offset: isize, val: isize) -> Result<(), Exit> {
        let opcode = self.read(self.ip)?;
        let arg = self.read(self.ip + offset)?;
        let mode = (opcode / 10isize.pow(offset as u32 + 1))%10;
        
        match mode {
            0 => self.write(arg, val),
            2 => self.write(self.base + arg, val),
            unknown => Err(Exit::IllegalMode(unknown)),
        }
    }
    
    pub fn step(&mut self, input: Option<isize>) -> Result<(), Exit> {
        let opcode = self.read(self.ip)?;
        let instruction = opcode % 100;
        
        match instruction {
            1 => {
                let a = self.param(1)?;
                let b = self.param(2)?;
                self.out(3, a+b)?;
                self.ip += 4;
                Ok(())
            }
            
            2=> {
                let a = self.param(1)?;
                let b = self.param(2)?;
                self.out(3, a*b)?;
                self.ip += 4;
                Ok(())
            }
            
            3 => {
                let a = input.ok_or(Exit::Input)?;
                self.out(1, a)?;
                self.ip += 2;
                Ok(())
            }
            
            4 => {
                let a = self.param(1)?;
                self.ip += 2;
                Err(Exit::Output(a))
            }
            
            5 => {
                let a = self.param(1)?;
                let b = self.param(2)?;
                if a != 0 {
                    self.ip = b;
                } else {
                    self.ip += 3;
                }
                Ok(())
            }
        
            6 => {
                let a = self.param(1)?;
                let b = self.param(2)?;
                if a == 0 {
                    self.ip = b;
                } else {
                    self.ip += 3;
                }
                Ok(())
            }
        
            7 => {
                let a = self.param(1)?;
                let b = self.param(2)?;
                self.out(3, if a < b { 1 } else { 0 })?;
                self.ip += 4;
                Ok(())
            }

            8 => {
                let a = self.param(1)?;
                let b = self.param(2)?;
                self.out(3, if a == b { 1 } else { 0 })?;
                self.ip += 4;
                Ok(())
            }

            99 => Err(Exit::Halted),
            
            unknown => Err(Exit::IllegalInstruction(unknown))
        }
        
    }
    
    pub fn resume(&mut self, mut input: Option<isize>) -> Exit {
        loop {
            match self.step(input.take()) {
                Ok(_) => {}
                Err(e) => return e,
            }
        }
    }    
    
    pub fn run<I, O>(&mut self, input: I, output: O) -> Exit
    where
        I: IntoIterator<Item = isize>,
        O: FnMut(isize),
    {
        let mut input = input.into_iter().peekable();
        let mut output = output;
        let mut next_input = None;
        loop {
            match self.resume(next_input.take()) {
                Exit::Input if input.peek().is_some() => {
                    next_input = input.next();
                }
                Exit::Output(a) => {
                    output(a);
                }
                other => return other,
            }
        }
    }
}

#[derive(Debug, PartialEq)]
pub enum Exit {
    NegativePointer,
    IllegamMode(isize),
    IllegalInstruction(isize),
    Input,
    Output(isize),
    Halted,
}

impl fmt::Display for Exit {
        fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
            match self {
                Exit::NegativePointer => write!(f, "attempted to use a negative value as pointer"),
                Exit::IllegalMode(mode) => write!(f, "illegal mode: {}", mode),
                Exit::IllegalInstruction(inst) => write!(f, "illegal instruction: {}", inst),
                Exit::Input => write!(f, "need input"),
                Exit::Output(a) => write!(f, "got output: {}", a),
                Exit::Halted => write!(f, "halted"),
            }
        }
    }
}


fn run(program: &[isize], input: &[isize]) -> (Machine, Exit, Vec<isize>) {
    let mut machine = Machine::with_program(program);
    let mut output = Vec::new();
    
    let exit = machine.run(input.iter().copied(), |a| output.push(a));
    (machine, exit, output)
}

fn day2() {
    let (machine, exit, _output) = run(&[1,9,10,3,2,3,11,0,99,30,40,50], &[]);
    assert_eq!(exit, Exit::Halted);
    assert_eq!(machine.mem()[0], 3500);
}
    
    